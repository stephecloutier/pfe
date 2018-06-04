from django import forms

from django.utils.translation import pgettext_lazy

from ..forms import OrderedModelMultipleChoiceField
from ..product.widgets import ImagePreviewWidget
from ...photos.models import Photo

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image', )
        labels = {
            'image': 'Image'}

    # def __init__(self, *args, **kwargs):
    #     product = kwargs.pop('product')
    #     super().__init__(*args, **kwargs)
    #     self.instance.product = product

    def save(self, commit=True):
        image = super().save(commit=commit)
        # create_product_thumbnails.delay(image.pk)
        return image


class PhotosImageForm(forms.ModelForm):
    use_required_attribute = False
    # variants = forms.ModelMultipleChoiceField(
    #     queryset=ProductVariant.objects.none(),
    #     widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Photo
        exclude = ('sort_order', )
        # exclude = ('product', 'sort_order')
        labels = {
            'image': 'Photo',
            'alt': pgettext_lazy(
                'Description', 'Description')}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.image:
            self.fields['image'].widget = ImagePreviewWidget()

    def save(self, commit=True):
        image = super().save(commit=commit)
        # create_product_thumbnails.delay(image.pk)
        return image

class ReorderPhotosImagesForm(forms.ModelForm):
    ordered_images = OrderedModelMultipleChoiceField(
        queryset=Photo.objects.none())

    class Meta:
        model = Photo
        fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['ordered_images'].queryset = Photo.objects.all()

    def save(self):
        for order, image in enumerate(self.cleaned_data['ordered_images']):
            image.sort_order = order
            image.save()
        return self.instance
