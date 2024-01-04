from django.views.decorators.http import require_http_methods
from django.shortcuts import render

@require_http_methods(["POST"])
def add_comment(request, id):
    return render(request, "")