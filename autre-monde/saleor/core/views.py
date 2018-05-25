import json
from pprint import pprint

from django.contrib import messages
from django.template.response import TemplateResponse
from django.utils.translation import pgettext_lazy
from impersonate.views import impersonate as orig_impersonate

from ..account.models import User
from ..dashboard.views import staff_member_required
from ..product.utils import products_for_homepage, coming_soon_products, new_products
from ..product.utils.availability import products_with_availability
from ..seo.schema.webpage import get_webpage_schema


def home(request):
    n_products = new_products()[:3]
    cs_products = coming_soon_products()[:3]

    n_products = products_with_availability(
        n_products, discounts=request.discounts, taxes=request.taxes,
        local_currency=request.currency)
    cs_products = products_with_availability(
        cs_products, discounts=request.discounts, taxes=request.taxes,
        local_currency=request.currency)
    webpage_schema = get_webpage_schema(request)
    return TemplateResponse(
        request, 'home.html', {
            'parent': None,
            'n_products': n_products,
            'cs_products': cs_products,
            'webpage_schema': json.dumps(webpage_schema)})


@staff_member_required
def styleguide(request):
    return TemplateResponse(request, 'styleguide.html')


def impersonate(request, uid):
    response = orig_impersonate(request, uid)
    if request.session.modified:
        msg = pgettext_lazy(
            'Impersonation message',
            'You are now logged as {}'.format(User.objects.get(pk=uid)))
        messages.success(request, msg)
    return response


def handle_404(request, exception=None):
    return TemplateResponse(request, '404.html', status=404)


def manifest(request):
    return TemplateResponse(
        request, 'manifest.json', content_type='application/json')
