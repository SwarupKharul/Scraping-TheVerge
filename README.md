# Scraping-TheVerge

This is a simple web scraper that scrapes the latest news from The Verge. It uses the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library to parse the HTML and [Requests](https://requests.readthedocs.io/en/master/) to get the HTML from the website.

The scrapper is deployed on AWS as a Lambda function. The function is triggered by an API Gateway endpoint. The endpoint is then used by a [Django](https://www.djangoproject.com/) app to store the scraped data in a database.

The AWS Lambda Function url is: https://4rv2gllqedqztv6k5id4zknon40kfdss.lambda-url.ap-south-1.on.aws