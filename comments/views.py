from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from forms import CommentForm
from models import Comment
import logging

"""
This function is activated when a form is submitted
    to add a new comment on an image
POST is the only allowed HTTP method because
    there is no corresponding page to render
The comment gets the author added based on the 
    logged in user and is then save to the database
"""
@require_http_methods(["POST"])
def add_comment(request, id):
    try:
        logging.debug("Entered into view function for adding comments")
        form = CommentForm(request.POST)
        if form.is_valid():
            logging.info("Submitted form to add comment is valid")
            comment:Comment = form.save(False)
            comment.author = request.user 
            logging.debug("Comment has associated user")
            comment.save()
            logging.debug("Comment is saved to the database")
        else:
            logging.warning("Submitted form to add comment is not valid")
        return redirect("one_image", id=id)
    except:
        logging.exception("An exception occurred when trying to add a comment")