from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse


# A simple view to render the index page
def index(request):
    blog_title = "Dynamic new title"
    return render(request, "index.html", {"blog_title": blog_title})

# Optionally, you can create more views for different pages or actions in your app. 

def details(request, post_id):
    return render(request, "detail.html")

def old_url_redirect(request):
    return redirect(reverse('blog:new_url')) # Redirects to the new URL

def new_url_redirect(request):
    return HttpResponse("This is the new URL") # Renders the new URL