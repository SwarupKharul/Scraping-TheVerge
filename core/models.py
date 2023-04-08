from django.db import models


class Article(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateTimeField()
    
    def __str__(self):
        return self.title