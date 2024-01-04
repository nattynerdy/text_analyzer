from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from images import views as images
from comments import views as comments
from django.shortcuts import redirect

def redirect_to_list_images(request):
    return redirect("images")

urlpatterns = [
    path("", redirect_to_list_images, name="home_page"),
    path("login", images.user_login, name="login"),
    path("admin/", admin.site.urls),
    path("analyze-image", images.analyze_image, name="analyze_image"),
    path("images", images.all_images, name="images"), 
    path("image/<int:id>", images.one_image, name="one_image"),
    path("image/<int:id>/comment", comments.add_comment, name="add_comment")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
