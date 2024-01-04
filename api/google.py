from google.cloud import vision
from dotenv import load_dotenv
import logging

"""
This function isolates the Google Image AI API functionality.
The input is the bytes of the image file to be analyzed
The output is any text that is found in the image
The function requires the .env file to be set up
    as described in the README so that the 
    API client can be properly authenticated
Documentation for the API used can be found here:
    https://cloud.google.com/vision/docs/ocr#vision_text_detection-python
"""
def detect_text(file_contents:bytes):
    logging.debug("Entered into function for Google API")
    return_value = ""
    try:
        logging.debug("Loading environment variable file")
        load_dotenv()
        logging.info("Environment variable loaded successfully")
        client = vision.ImageAnnotatorClient()
        logging.info("Starting up Google API client")
        image = vision.Image(content=file_contents)
        logging.debug("Sending image to the Google API client")
        response = client.text_detection(image=image)
        logging.info("Response from client recieved")
        texts = response.text_annotations
        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(response.error.message)
            )
        return_value += "Discovered Text:"
        for text in texts:
            logging.debug("Text found:", text.description)
            return_value += f' "{text.description}",'
            logging.debug("Current return value state:", return_value)
        return_value = return_value[:-1]
    except:
        logging.exception("Error occurred in Google API function")
    finally:
        return return_value

