from django.db import models


class Category(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category_subcategory'
    )

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.TextField()
    isbn = models.TextField(null=True, blank=True)
    pagecount = models.IntegerField(null=True, blank=True)
    publisheddate = models.TextField(null=True, blank=True)
    thumbnailurl = models.TextField(null=True, blank=True)
    shortdescription = models.TextField(null=True, blank=True)
    longdescription = models.TextField(null=True, blank=True)
    status = models.TextField(blank=True)
    authors = models.ManyToManyField(
        Author,
        blank=True,
        related_name='authors_book'
    )
    categories = models.ManyToManyField(
        Category,
        blank=True,
        related_name='categories_book'
    )
    subcategories = models.ManyToManyField(
        SubCategory,
        blank=True,
        related_name='subcategories_book'
    )

    def __str__(self):
        return self.title


class FeedBack(models.Model):
    email = models.EmailField(blank=True)
    name = models.TextField(blank=True)
    comment = models.TextField(blank=True)
    phone = models.TextField(blank=True)

    def __str__(self):
        return self.comment
