from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from comments.forms import CommentForm
from comments.models import Comment
from images.models import ImageUpload
import logging

"""
This function is activated when a form is submitted
    to add a new comment on an image
POST is the only allowed HTTP method because
    there is no corresponding page to render
The comment gets the author added based on the 
    logged in user and is then save to the database
"""
@login_required
@require_http_methods(["POST"])
def add_comment(request, id):
    try:
        logging.debug("Entered into view function for adding comments for image with id", str(id))
        form = CommentForm(request.POST)
        if form.is_valid():
            logging.info("Submitted form to add comment is valid")
            comment:Comment = form.save(False)
            comment.author = request.user 
            logging.debug("Comment has associated user")
            comment.image = get_object_or_404(ImageUpload, id=id)
            logging.debug("Comment has associated image")
            comment.save()
            logging.debug("Comment is saved to the database")
        else:
            logging.warning("Submitted form to add comment is not valid")
    except:
        logging.exception("An exception occurred when trying to add a comment")
    finally:
        return redirect("one_image", id=id)