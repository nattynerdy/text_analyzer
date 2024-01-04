from django.db import models
from django.conf import settings

class Comment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="comments",
        on_delete=models.CASCADE,
        null=True
    )
    image = models.ForeignKey(
        "ImageUpload",
        related_name="comments",
        on_delete=models.CASCADE
    )
    text = models.TextField()
