from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from forms import CommentForm
from models import Comment

@require_http_methods(["POST"])
def add_comment(request, id):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment:Comment = form.save(False)
        comment.author = request.user 
        comment.save()
    return redirect("one_image", id=id)