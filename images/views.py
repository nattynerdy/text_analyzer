from django.shortcuts import render
from django.http import HttpRequest
from forms import ImageForm
from models import ImageUpload
from api import google
import logging

def analyze_image(request:HttpRequest):
    try:
        logging.debug("Entered into view function for analyzing images")
        if request.method == "POST":
            logging.debug("POST request received")
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
        return render(request, "")
    except:
        logging.exception("An exception occurred when trying to upload an image")
        
def all_images(request):
    return render(request, "")

def one_image(request, id):
    return render(request, "")