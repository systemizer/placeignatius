from django.core.management.base import BaseCommand, CommandError
from placeignatius.main.models import PlaceImage

class Command(BaseCommand):

    def handle(self, *args, **options):
        for placeimage in PlaceImage.objects.all():
            placeimage.width = placeimage.image.width
            placeimage.height = placeimage.image.height
            placeimage.aspect_ratio = float(placeimage.image.width) / placeimage.height
