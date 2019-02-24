from django.db import models

# Create your models here.


class Gallery(models.Model):
    description = models.CharField(default='', max_length=100)
    image = models.ImageField(default='',upload_to='image/')
    title = models.CharField(default= '标题',max_length=50)

    def __str__(self):
        return self.title