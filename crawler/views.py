from django.http import JsonResponse
from django.shortcuts import render

from crawler.tasks import crawl_task

# Create your views here.


def start_crawl(request):
    url = request.Get().get("url", "")
    if not url:
        return JsonResponse({"error": "URL parameter is required"}, status=400)
    crawl_task.delay(url)
    return JsonResponse({"message": "Crawling started", "url": url})
