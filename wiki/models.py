from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.title }"
