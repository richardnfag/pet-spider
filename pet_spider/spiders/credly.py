import scrapy
from ..settings import BUCKET_NAME, CREDLY_USERNAME

class CredlySpider(scrapy.Spider):
    name = "credly"
    custom_settings = {
        "FEEDS": {f"s3://{BUCKET_NAME}/credly.json": {"format": "json", "encoding": "utf8"}}
    }

    def start_requests(self):
        yield scrapy.Request(
            f"https://www.credly.com/users/{CREDLY_USERNAME}/badges?sort=-state_updated_at&page=1",
        )

    def parse(self, response):
        for badges in response.css(".cr-public-earned-badge-grid-item"):
            yield {
                "title": (
                    badges.css(".cr-public-earned-badge-grid-item::attr(title)").get()
                ),
                "reference": (
                    "https://credly.com" + badges.css(".cr-public-earned-badge-grid-item::attr(href)").get()
                ),
                "image_url": (
                    badges.css(".cr-public-earned-badge-grid-item img::attr(src)").get().replace("110x110", "220x220")
                ),
            }
