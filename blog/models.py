from django.db import models

# Create your models here.


class Blog(models.Model):

    title = models.CharField(default='文章标题', max_length=50)
    date = models.DateField()
    image = models.ImageField(default='default.png')
    text = models.CharField(default='正文', max_length=10000)


    def __str__(self):
        return self.title

    def short_text(self):
        return self.text[:70] + '...'