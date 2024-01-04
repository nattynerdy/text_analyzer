from django.db import models
from django.conf import settings

class Comment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="recipes",
        on_delete=models.CASCADE,
        null=True
    )
    text = models.TextField()
