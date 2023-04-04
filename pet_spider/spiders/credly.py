import scrapy


class CredlySpider(scrapy.Spider):
    name = "credly"
    custom_settings = {
        "FEEDS": {"s3://spider/credly.json": {"format": "json", "encoding": "utf8"}}
    }

    def start_requests(self):
        username = self.settings.get("CREDLY_USERNAME")

        yield scrapy.Request(
            f"https://www.credly.com/users/{username}/badges?sort=-state_updated_at&page=1",
        )

    def parse(self, response):
        for badges in response.css(".cr-public-earned-badge-grid-item"):
            yield {
                "title": (
                    badges.css(".cr-public-earned-badge-grid-item::attr(title)").get()
                ),
                "reference": (
                    badges.css(".cr-public-earned-badge-grid-item::attr(href)").get()
                ),
                "image_url": (
                    badges.css(".cr-public-earned-badge-grid-item img::attr(src)").get()
                ),
            }
