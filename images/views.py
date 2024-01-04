from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from forms import ImageForm
from models import ImageUpload
from ..api import google
import logging

"""
This function is activated when a form is submitted
    to upload a new image for processing
POST is the only allowed HTTP method because
    there is no corresponding page to render
The image is pulled from the submitted form and
    sent to the Google Image AI API for processing
Then, the image is saved to the database with the
    text that was received from the API
"""
@require_http_methods(["POST"])
def analyze_image(request:HttpRequest):
    try:
        logging.debug("Entered into view function for analyzing images")
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            logging.info("Submitted form to analyze image is valid")
            image_upload:ImageUpload = form.save(False)
            logging.debug("Reading file contents")
            file_contents = image_upload.image.read()
            logging.debug("Sending file contents to Google API")
            image_text = google.detect_text(file_contents)
            if image_text is not "":
                logging.info("Text from Google API is ", image_text)
                image_upload.text = image_text
                image_upload.save()
                logging.debug("Image is saved to the database")
            else:
                logging.warning("No image text returned from Google API")
        else:
            logging.warning("Submitted form to analyze image is not valid")
        return redirect("images")
    except:
        logging.exception("An exception occurred when trying to upload an image")

"""
This function renders the main page of the application
It is GET only because any forms on it have an action
    that go to a different URL to manipulate data
The main page has all the uplaoded images on it,
    and they render with infinite scrolling.
"""
@require_http_methods(["GET"])
def all_images(request):
    try:
        logging.debug("Entered into view function for loading all images")
        images = ImageUpload.objects.all()
        logging.info("Retrieved", str(images.count()), "image objects")
        form = ImageForm()
        context = {
            "images": images,
            "form": form
        }
        logging.debug("About to render page")
        return render(request, "list.html", context)
    except:
        logging.exception("An exception occurred when trying to load all the images")

"""
This function renders the detail page for any image
    uploaded to the application with its comments
It is GET only because any forms on it have an action
    that go to a different URL to manipulate data
This page has all the comments associated with an 
    image on it, and they render with infinite scrolling.
"""
@require_http_methods(["GET"])
def one_image(request, id):
    try:
        logging.debug("Entered into view function for loading image detail page")
        image = get_object_or_404(ImageUpload, id=id)
        logging.info("Retrieved image object with id", id)
        context = {
            "image_upload": image
        }
        logging.debug("About to render page")
        return render(request, "detail.html", context)
    except:
        logging.exception("An exception occurred when trying to load details on an image")