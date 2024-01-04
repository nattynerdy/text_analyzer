from google.cloud import vision
from dotenv import load_dotenv
import logging

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
        logging.debug("Response from client recieved")
        texts = response.text_annotations
        return_value += "Texts:"
        for text in texts:
            logging.debug("Text found:", text.description)
            return_value += f'\n"{text.description}"'
            vertices = [
                f"({vertex.x},{vertex.y})" for vertex in text.bounding_poly.vertices
            ]
            bounds = "bounds: {}".format(",".join(vertices))
            logging.debug("Text bounds:", bounds)
            return_value += bounds
            logging.debug("Current return value state:", return_value)
        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(response.error.message)
            )
    except:
        logging.exception("Error occurred in Google API function")
    finally:
        return return_value

