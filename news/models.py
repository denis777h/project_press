from django.db import models
from datetime import datetime


# Create your models here.

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateTimeField(datetime)


    def __str__(self):
        return self.title

    def __str__(self):
        return self.publication_date.__str__()



