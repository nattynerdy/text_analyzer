from django.test import TestCase

class CommentTests(TestCase):
    def comment_model_exists(self):
        try:
            from comments.models import Comment
        except ModuleNotFoundError:
            self.fail("No model found")
    
    
