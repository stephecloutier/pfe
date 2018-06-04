from ..product.widgets import ImagePreviewWidget
from ...photos.models import PhotoImage

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = PhotoImage
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
        model = ProductImage
        exclude = ('product', 'sort_order')
        labels = {
            'image': pgettext_lazy('Product image', 'Image'),
            'alt': pgettext_lazy(
                'Description', 'Description')}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.image:
            self.fields['image'].widget = ImagePreviewWidget()

    def save(self, commit=True):
        image = super().save(commit=commit)
        create_product_thumbnails.delay(image.pk)
        return image