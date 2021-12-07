from django.db import models

# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='user_profile')
    description = models.TextField()
    phone = models.CharField(max_length=21)
    email = models.EmailField(max_length=100)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name