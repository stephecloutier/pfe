from pprint import pprint
from urllib.parse import urlencode

from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.db.models import F, Q

from ...cart.utils import (
    get_cart_from_request, get_or_create_cart_from_request)
from ...core.utils import get_paginator_items
from ...core.utils.filters import get_now_sorted_by
from ..forms import ProductForm
from .availability import products_with_availability

from datetime import date, timedelta
from django.utils import timezone

def products_visible_to_user(user):
    # pylint: disable=cyclic-import
    from ..models import Product
    if user.is_authenticated and user.is_active and user.is_staff:
        return Product.objects.all()
    return Product.objects.available_products()


def products_with_details(user):
    products = products_visible_to_user(user)
    products = products.prefetch_related(
        'category', 'images', 'variants__variant_images__image',
        'attributes__values', 'product_type__product_attributes__values')
    return products    

def product_custom_details(product):
    product.release_status = None
    if product.release_date > date.today():
        product.release_status = 'cs'
    elif ((date.today() - product.release_date) <= timedelta(weeks=4)):
        product.release_status = 'news'
    
    amount = product.price.amount
    if amount <= 10:
        product.price_indicator = range(1)
    elif amount <= 30:
        product.price_indicator = range(2)
    elif amount <= 40:
        product.price_indicator = range(3)
    else :
        product.price_indicator = range(4)
    
    return product

def products_for_homepage():
    user = AnonymousUser()
    products = products_with_details(user)
    products = products.filter(is_featured=True)
    return products

def coming_soon_products():
    user = AnonymousUser()
    products = products_with_details(user)
    products = products.filter(release_date__gt=date.today())
    # Custom details  
    for product in products:
        product = product_custom_details(product)
    return products

def new_products():
    user = AnonymousUser()
    products = products_with_details(user)
    products = products.filter(release_date__lte=date.today(), release_date__gte=date.today() - timedelta(weeks=4)).order_by('-release_date')
    # Custom details  
    for product in products:
        product = product_custom_details(product)
    return products

def all_products():
    user = AnonymousUser()
    products = products_with_details(user)
    # Custom details  
    for product in products:
        product = product_custom_details(product)
    return products

def get_product_images(product):
    """Return list of product images that will be placed in product gallery."""
    return list(product.images.all())


def handle_cart_form(request, product, create_cart=False):
    if create_cart:
        cart = get_or_create_cart_from_request(request)
    else:
        cart = get_cart_from_request(request)
    form = ProductForm(
        cart=cart, product=product, data=request.POST or None,
        discounts=request.discounts, taxes=request.taxes)
    return form, cart


def products_for_cart(user):
    products = products_visible_to_user(user)
    products = products.prefetch_related('variants__variant_images__image')
    return products


def get_variant_url_from_product(product, attributes):
    return '%s?%s' % (product.get_absolute_url(), urlencode(attributes))


def get_variant_url(variant):
    attributes = {
        str(attribute.pk): attribute
        for attribute in variant.product.product_type.variant_attributes.all()}
    return get_variant_url_from_product(variant.product, attributes)


def allocate_stock(variant, quantity):
    variant.quantity_allocated = F('quantity_allocated') + quantity
    variant.save(update_fields=['quantity_allocated'])


def deallocate_stock(variant, quantity):
    variant.quantity_allocated = F('quantity_allocated') - quantity
    variant.save(update_fields=['quantity_allocated'])


def decrease_stock(variant, quantity):
    variant.quantity = F('quantity') - quantity
    variant.quantity_allocated = F('quantity_allocated') - quantity
    variant.save(update_fields=['quantity', 'quantity_allocated'])


def increase_stock(variant, quantity, allocate=False):
    """Return given quantity of product to a stock."""
    variant.quantity = F('quantity') + quantity
    update_fields = ['quantity']
    if allocate:
        variant.quantity_allocated = F('quantity_allocated') + quantity
        update_fields.append('quantity_allocated')
    variant.save(update_fields=update_fields)


def get_product_list_context(request, filter_set):
    """
    :param request: request object
    :param filter_set: filter set for product list
    :return: context dictionary
    """
    # Avoiding circular dependency
    from ..filters import SORT_BY_FIELDS
    products_paginated = get_paginator_items(
        filter_set.qs, settings.PAGINATE_BY, request.GET.get('page'))  
    for product in products_paginated.object_list:
        product = product_custom_details(product)
    products_and_availability = list(products_with_availability(
        products_paginated, request.discounts, request.taxes,
        request.currency))
    now_sorted_by = get_now_sorted_by(filter_set)
    arg_sort_by = request.GET.get('sort_by')
    is_descending = arg_sort_by.startswith('-') if arg_sort_by else False
    return {
        'filter_set': filter_set,
        'products': products_and_availability,
        'products_paginated': products_paginated,
        'sort_by_choices': SORT_BY_FIELDS,
        'now_sorted_by': now_sorted_by,
        'is_descending': is_descending}

def get_product_list_context_without_filter(request, items):
    """
    :param request: request object
    :return: context dictionary
    """
    products_paginated = get_paginator_items(
        items, settings.PAGINATE_BY, request.GET.get('page'))  
    for product in products_paginated.object_list:
        product = product_custom_details(product)
    products_and_availability = list(products_with_availability(
        products_paginated, request.discounts, request.taxes,
        request.currency))
    return {
        'products': products_and_availability,
        'products_paginated': products_paginated,
       }

def get_product_list_sorted_context(request):
    """
    :param request: request object
    :return: context dictionary
    """
    # Avoiding circular dependency
    from ..filters import SORT_BY_FIELDS
    
    now_sorted_by = get_now_sorted_by(filter_set) ##TO DO
    arg_sort_by = request.GET.get('sort_by')
    is_descending = arg_sort_by.startswith('-') if arg_sort_by else False
    return {
        'sort_by_choices': SORT_BY_FIELDS,
        'now_sorted_by': now_sorted_by,
        'is_descending': is_descending}


def collections_visible_to_user(user):
    # pylint: disable=cyclic-import
    from ..models import Collection
    if user.is_authenticated and user.is_active and user.is_staff:
        return Collection.objects.all()
    return Collection.objects.public()