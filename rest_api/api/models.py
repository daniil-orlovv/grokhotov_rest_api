from django.db import models


class Book(models.Model):
    title = models.TextField()
    isbn = models.TextField()
    pageCount = models.IntegerField()
    publishedDate = models.TextField()
    thumbnailUrl = models.TextField()
    status = models.TextField()
    authors = models.JSONField()
    categories = models.JSONField()


class FeedBack(models.Model):
    email = models.EmailField()
    name = models.TextField()
    comment = models.TextField()
    phone = models.TextField()
