from django.db import models
from ..core.models import SortableModel

from versatileimagefield.fields import PPOIField, VersatileImageField


# Create your models here.

class Photo(SortableModel):
    
    image = VersatileImageField(
        upload_to='photos', ppoi_field='ppoi', blank=False)
    ppoi = PPOIField()
    alt = models.CharField(max_length=128, blank=True)

    class Meta:
        ordering = ('sort_order', )
        # app_label = 'product'

    # def get_ordering_queryset(self):
    #     return self.photos.images.all()