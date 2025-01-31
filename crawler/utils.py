from bs4 import BeautifulSoup
import requests

from crawler.models import CrawledPage


def crawl_page(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title else "No Title"
        content = soup.get_text()

        page, created = CrawledPage.objects.get_or_create(
            url, defaults={"title": title, "content": content}
        )
        return {
            "url": url,
            "title": title,
            "status": "Created" if created else "Already Exists",
        }
    except Exception as e:
        return {"Url": url, "error": str(e)}
