from celery import shared_task
from crawler.utils import crawl_page


@shared_task
def crawl_task(url):
    return crawl_page(url)
