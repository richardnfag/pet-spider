# Pet Spider

## Environment variables

Define follow environment variables:

```sh
CREDLY_USERNAME="<my-credly-username>"
GITHUB_USERNAME="<my-github-username>"
GITHUB_TOKEN="<my-github-token>"

AWS_ACCESS_KEY_ID="<s3-access-key>"
AWS_SECRET_ACCESS_KEY="<s3-secret-key>"
AWS_ENDPOINT_URL="<s3-endpoint>"

# AWS_USE_SSL=False
# Use this option if you want to disable SSL connection for communication with S3 storage.
# By default SSL will be used.
```

## Extracted data

Credly Badges

```json
[
    {
        "title": "Web Scraping Python - Advanced",
        "reference": "/badges/6340f4ff-d4b7-499a-96bd-5c4730e8a2c9",
        "image_url": "https://images.credly.com/6340f4ff-d4b7-499a-96bd-5c4730e8a2c9/image.png"
    },
]
```

GitHub Repositories

```json
[
    {
        "id": 1000,
        "name": "pet-spider",
        "description": "My personal web crawler",
        "languages": [
            {
                "name": "Python",
                "size": 1610,
                "color": "#3572A5"
            }
        ]
    },
]
```
## You can run a spider using the scrapy crawl command, such as:

```sh
scrapy crawl credly
```

```sh
scrapy crawl github
```
