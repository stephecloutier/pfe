from celery import shared_task

from ..core.utils import create_thumbnails
from .models import ProductImage
from ..photos.models import Photo


@shared_task
def create_product_thumbnails(image_id):
    """Takes ProductImage model, and creates thumbnails for it."""
    create_thumbnails(pk=image_id, model=ProductImage, size_set='products')

@shared_task
def create_photos_thumbnails(image_id):
    """Takes PhotoImage model, and creates thumbnails for it."""
    create_thumbnails(pk=image_id, model=Photo, size_set='products')