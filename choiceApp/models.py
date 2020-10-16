from django.db import models

class Photo(models.Model):
    photo=models.ImageField(blank=True)


class Test(models.Model):
    name=models.CharField(max_length=35)
    author=models.CharField(max_length=40)
    photo=models.ManyToManyField(Photo)
    avatar=models.ImageField(blank=True)
    def __str__(self):
        return self.name