from django.urls import path
from . import views
app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:post_id>", views.details, name="details"),
    path("old_url", views.old_url_redirect, name="old_url"),
    path("This_is_new_url", views.new_url_redirect, name="new_url"),
]