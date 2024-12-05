from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse


# A simple view to render the index page
def index(request):
    blog_title = "Dynamic new title"
    posts = [
        {'id': 1, 'title': 'Post 1', 'content': 'This is the first post'},
        {'id': 2,'title': 'Post 2', 'content': 'This is the second post'},
        {'id': 3,'title': 'Post 3', 'content': 'This is the third post'},   
        {'id': 4,'title': 'Post 4', 'content': 'This is the fourth post'},
    ]
    return render(request, "index.html", {"blog_title": blog_title})

# Optionally, you can create more views for different pages or actions in your app. 

def details(request, post_id):
    return render(request, "detail.html")

def old_url_redirect(request):
    return redirect(reverse('blog:new_url')) # Redirects to the new URL

def new_url_redirect(request):
    return HttpResponse("This is the new URL") # Renders the new URL