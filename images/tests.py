from django.test import TestCase, Client

class ImageTests(TestCase):
    def image_model_exists(self):
        try:
            from images.models import ImageUpload
        except ModuleNotFoundError:
            self.fail("No model found")
    
    def test_list_response_is_200(self):
            client = Client()
            response = client.get("/images")
            if (
                response.status_code != 302
                or not response.has_header("Location")
            ):
                self.assertEqual(
                    response.status_code,
                    200,
                    msg="Did not get a 200 OK for the path images/",
                )

