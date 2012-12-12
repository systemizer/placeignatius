from django.core.management.base import BaseCommand, CommandError
from placeignatius.main.models import PlaceImage

from django.core.files import File

import os
from os import listdir
from os.path import isfile, join

this_path = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))
images_path = "%s/images" % this_path
image_files = [ "%s/%s" % (images_path,f) for f in listdir(images_path) if isfile(join(images_path,f)) ]

class Command(BaseCommand):
    def handle(self, *args, **options):
        for image_f in image_files:
            PlaceImage(image=File(open(image_f,'rb'))).save()
