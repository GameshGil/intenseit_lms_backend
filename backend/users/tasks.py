from PIL import Image
from celery import shared_task


@shared_task
def generate_thumbnail(source_path, thumbnail_path, size=(64, 64)):
    with Image.open(source_path) as img:
        img.thumbnail(size)
        img.save(thumbnail_path)
