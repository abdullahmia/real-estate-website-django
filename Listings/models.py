from django.db import models
from Realtors.models import Realtor
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = RichTextUploadingField(null=True)
    price = models.IntegerField(default=0)
    bedrooms = models.IntegerField(default=0)
    barthrooms = models.IntegerField(default=0)
    sqft = models.IntegerField(default=0)
    garage = models.IntegerField(default=0)
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos')
    photo_1 = models.ImageField(upload_to='photos', blank=True)
    photo_2 = models.ImageField(upload_to='photos', blank=True)
    photo_3 = models.ImageField(upload_to='photos', blank=True)
    photo_4 = models.ImageField(upload_to='photos', blank=True)
    photo_5 = models.ImageField(upload_to='photos', blank=True)
    photo_6 = models.ImageField(upload_to='photos', blank=True)
    is_puslished = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title