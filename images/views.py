from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
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
        return redirect()
    except:
        logging.exception("An exception occurred when trying to upload an image")

def all_images(request):
    return render(request, "")

def one_image(request, id):
    return render(request, "")