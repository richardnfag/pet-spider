import scrapy
import yaml
from ..settings import BUCKET_NAME, GITHUB_USERNAME, GITHUB_TOKEN

LINGUIST_URL = "https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml"


class GithubSpider(scrapy.Spider):
    name = "github"
    custom_settings = {
        "FEEDS": {f"s3://{BUCKET_NAME}/github.json": {"format": "json", "encoding": "utf8"}}
    }

    def start_requests(self):
        self.headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        yield scrapy.Request(LINGUIST_URL, callback=self.parse_language_colors)
        yield scrapy.Request(
            f"https://api.github.com/users/{GITHUB_USERNAME}/repos",
            headers=self.headers,
        )

    def parse(self, response):
        for repo in response.json():
            if not repo["fork"]:

                request = scrapy.Request(
                    repo["languages_url"],
                    headers=self.headers,
                    callback=self.parse_languages,
                    cb_kwargs={
                        "id": repo["id"],
                        "name": repo["name"],
                        "description": repo["description"],
                    },
                )

                yield request

    def parse_languages(self, response, id, name, description):
        yield {
            "id": id,
            "name": name,
            "description": description,
            "languages": [
                {
                    "name": name,
                    "size": size,
                    "color": self.language_colors.get(name),
                }
                for name, size in response.json().items()
            ],
        }

    def parse_language_colors(self, response):
        self.language_colors = {
            language: values.get("color")
            for language, values in yaml.safe_load(response.body).items()
        }
