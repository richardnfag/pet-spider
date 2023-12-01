FROM python:3.11.1-slim-bullseye

WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip install requirements.txt

CMD ["/bin/bash", "-c", "scrapy crawl credly; scrapy crawl github" ]
