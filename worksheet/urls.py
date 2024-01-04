"""
URL configuration for worksheet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from images import views as images
from comments import views as comments

urlpatterns = [
    path("admin/", admin.site.urls),
    path("analyze-image", images.analyze_image, name="analyze_image"),
    path("images", images.all_images, name="images"), 
    path("image/<int:id>", images.one_image, name="one_image"),
    path("image/<int:id>/comment", comments.add_comment, name="add_comment")
]
