from django.urls import path, include
from .views import helloAPI, sign_up, show_users, log_in, get_feeds, post_feed

urlpatterns = [
    path("hello/", helloAPI),
    path("signUp/", sign_up),
    path("showUsers/", show_users),
    path("logIn/", log_in),
    path("feed/", get_feeds),
    path("post/", post_feed),
]
