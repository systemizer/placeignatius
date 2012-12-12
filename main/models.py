from django.db import models
import random

STANDARD_ASPECT_RATIOS = [1.33,1.41,1.5,1.6,1.66,1.77,1.85,2.39]

ASPECT_RATIO_CHOICES = [(x,x) for x in STANDARD_ASPECT_RATIOS]

# Create your models here.
class PlaceImage(models.Model):
    image = models.ImageField(upload_to="placeimages")
    aspect_ratio = models.DecimalField(decimal_places=4,max_digits=10,null=True,blank=True,choices=ASPECT_RATIO_CHOICES)
    height = models.IntegerField(null=True,blank=True)
    width = models.IntegerField(null=True,blank=True)

    def __unicode__(self):
        return self.image.name

    def save(self):
        self.height = self.image.height
        self.width = self.image.width
        self.aspect_ratio = self.__class__._calculate_aspect_ratio(self.width,self.height)
        return super(PlaceImage,self).save()

    @classmethod
    def fetch_image(cls,width,height):
        aspect_ratio = cls._calculate_aspect_ratio(width,height)
        query = cls.objects.filter(aspect_ratio=str(aspect_ratio))
        if not query.exists():
            query = cls.objects.all()
        return random.sample(query,1)[0]

    @classmethod
    def _calculate_aspect_ratio(cls,width,height):
        real_aspect_ratio = float(width)/int(height)
        diff_aspect_ratios = [abs(x-real_aspect_ratio) for x in STANDARD_ASPECT_RATIOS]
        best_index = diff_aspect_ratios.index(min(diff_aspect_ratios))
        return STANDARD_ASPECT_RATIOS[best_index]
