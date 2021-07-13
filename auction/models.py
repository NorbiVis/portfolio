from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    slug = models.SlugField(null=True, blank=True)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='up_images/')
    time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    time = models.DateTimeField(auto_now_add=True)


class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watched")
    auction = models.ForeignKey(Product, on_delete=models.CASCADE)
