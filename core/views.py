import datetime
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
import requests
from .models import Article

seedurl = "https://4rv2gllqedqztv6k5id4zknon40kfdss.lambda-url.ap-south-1.on.aws"


def home(request):
    return JsonResponse(
        {"message": "Hello Scrapper!", "urls": {"csv": "/csv", "updatedb": "/updatedb"}}
    )


def updatedb(request):
    if request.method == "GET":
        # Fetch data from the seed url
        response = requests.get(seedurl)
        content = response.content

        # Upload the data to db
        for article in content:
            try:
                Article.objects.create(
                    id=article["id"],
                    title=article["title"],
                    url=article["url"],
                    author=article["author"],
                    date=article["date"],
                )
            # If the article already exists, update it
            except IntegrityError:
                Article.objects.filter(id=article["id"]).update(
                    title=article["title"],
                    url=article["url"],
                    author=article["author"],
                    date=article["date"],
                )
        return JsonResponse({"message": "Database updated successfully."})
    else:
        return JsonResponse({"error": "Only GET requests are allowed."})


def csv(request):
    if request.method == "GET":
        # Fetch data from database
        articles = Article.objects.all()

        # Convert the data to csv
        csv = "id,title,url,author,date\n"
        for article in articles:
            csv += f"{article.id},{article.title},{article.url},{article.author},{article.date}\n"

        # Return the ddmmyyy_verge.csv file
        name = f"{datetime.datetime.now().strftime('%d%m%Y')}_verge.csv"

        response = HttpResponse(csv, content_type="text/csv")
        response["Content-Disposition"] = f"attachment; filename={name}"

        return response
