from django.shortcuts import render
from django.http import HttpRequest
from forms import ImageForm

def analyze_image(request:HttpRequest):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, "")

def all_images(request):
    return render(request, "")

def one_image(request, id):
    return render(request, "")