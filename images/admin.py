from django.contrib import admin
from images.models import ImageUpload

@admin.register(ImageUpload)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "text"
    )
