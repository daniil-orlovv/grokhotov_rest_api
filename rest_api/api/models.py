from django.db import models


class Category(models.Model):
    title = models.TextField()


class Author(models.Model):
    name = models.TextField()


class Book(models.Model):
    title = models.TextField()
    isbn = models.TextField(null=True, blank=True)
    pagecount = models.IntegerField(null=True, blank=True)
    publisheddate = models.TextField(null=True, blank=True)
    thumbnailurl = models.TextField(null=True, blank=True)
    shortdescription = models.TextField(null=True, blank=True)
    longdescription = models.TextField(null=True, blank=True)
    status = models.TextField()
    authors = models.ManyToManyField(
        Author,
        blank=True
    )
    categories = models.ManyToManyField(
        Category,
        blank=True
    )


class Subcategory(models.Model):
    title = models.TextField()
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='book_subcategories'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category_subcategories'
    )


class FeedBack(models.Model):
    email = models.EmailField()
    name = models.TextField()
    comment = models.TextField()
    phone = models.TextField()
