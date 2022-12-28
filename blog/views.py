from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
# post = [
# {
# 'author' : 'Sherrif',
# 'title' : 'Blog post',
# 'content': 'First content',
# 'date_posted': 'December 20, 2022'
# },
# {
# 'author' : 'BSherrif',
# 'title' : 'Blog post2',
# 'content': 'Second content',
# 'date_posted': 'December 20, 2022'
# }
# ]
def about(request):
    return render(request, "blog/about.html", {"title": "About"})


def home(request):
    context = {"poster": Post.objects.all()}
    return render(request, "blog/home.html", context)


def king(request):
    return HttpResponse("I will make it")
