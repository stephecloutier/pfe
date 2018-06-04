from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.decorators.http import require_POST


from ..views import staff_member_required
from ...photos.models import Photo

@staff_member_required
# @permission_required('product.view_product')
def photos_list(request):
    images = Photo.objects.all()
    ctx = {'images': images}#, 'is_empty': not images.exists()}
    return TemplateResponse(
        request, 'dashboard/photos/list.html', ctx)


@staff_member_required
# @permission_required('product.edit_product')
def photos_image_create(request):
    # product = get_object_or_404(Product, pk=product_pk)
    image = Photo()
    form = forms.PhotosImageForm(
        request.POST or None, request.FILES or None, instance=image)
    if form.is_valid():
        image = form.save()
        msg = pgettext_lazy(
            'Dashboard message',
            'Added image %s') % (image.image.name,)
        messages.success(request, msg)
        return redirect('dashboard:photos-list')
    ctx = {'form': form, 'image': image}
    return TemplateResponse(
        request,
        'dashboard/photos/form.html',
        ctx)


@staff_member_required
# @permission_required('product.edit_product')
def photos_image_edit(request, img_pk):
    image = get_object_or_404(pk=img_pk) #product.images,
    form = forms.PhotosImageForm(
        request.POST or None, request.FILES or None, instance=image)
    if form.is_valid():
        image = form.save()
        msg = pgettext_lazy(
            'Dashboard message',
            'Updated image %s') % (image.image.name,)
        messages.success(request, msg)
        return redirect('dashboard:photos-list')
    ctx = {'form': form, 'image': image}
    return TemplateResponse(
        request,
        'dashboard/photos/form.html',
        ctx)


@staff_member_required
# @permission_required('product.edit_product')
def photos_image_delete(request, img_pk):
    image = get_object_or_404(pk=img_pk) #product.images,
    if request.method == 'POST':
        image.delete()
        msg = pgettext_lazy(
            'Dashboard message', 'Removed image %s') % (image.image.name,)
        messages.success(request, msg)
        return redirect('dashboard:photos-list')
    return TemplateResponse(
        request,
        'dashboard/photos/modal/confirm_delete.html',
        {'product': product, 'image': image})


@require_POST
@staff_member_required
def ajax_upload_image(request):
    form = forms.UploadImageForm(
        request.POST or None, request.FILES or None)
    ctx = {}
    status = 200
    if form.is_valid():
        image = form.save()
        ctx = {'id': image.pk, 'image': None, 'order': image.sort_order}
    elif form.errors:
        status = 400
        ctx = {'error': form.errors}
    return JsonResponse(ctx, status=status)


@require_POST
@staff_member_required
def ajax_reorder_photos_images(request):
    form = forms.ReorderProductImagesForm(request.POST, instance=photos) #??
    status = 200
    ctx = {}
    if form.is_valid():
        form.save()
    elif form.errors:
        status = 400
        ctx = {'error': form.errors}
    return JsonResponse(ctx, status=status)
