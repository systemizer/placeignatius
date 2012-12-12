from django.db import models
import random

# Create your models here.
class PlaceImage(models.Model):
    image = models.ImageField(upload_to="placeimages")
    aspect_ratio = models.DecimalField(decimal_places=4,max_digits=10,null=True,blank=True)
    height = models.IntegerField(null=True,blank=True)
    width = models.IntegerField(null=True,blank=True)

    def __unicode__(self):
        return self.image.name

    @classmethod
    def fetch_image(cls,width,height):
        return random.sample(PlaceImage.objects.all(),1)[0]
