from django.urls import path
from .views import start_crawl

urlpatterns = [
    path("crawl/", start_crawl, name="start_crawl"),
]
