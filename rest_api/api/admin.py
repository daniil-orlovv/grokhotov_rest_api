from django.contrib import admin

from .models import (Book, Author, Category, SubCategory)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


class SubCategoryInlineAdmin(admin.TabularInline):
    model = Book.subcategories.through
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


class CategoryInlineAdmin(admin.TabularInline):
    model = Book.categories.through
    extra = 1


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class AuthorInlineAdmin(admin.TabularInline):
    model = Book.authors.through
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [
        AuthorInlineAdmin,
        CategoryInlineAdmin,
        SubCategoryInlineAdmin,]
    list_display = (
        'title',
        'isbn',
        'pagecount',
        'publisheddate',
        'thumbnailurl',
        'shortdescription',
        'longdescription',
        'status',
    )
    list_filter = ('categories',
                   'title',
                   'status',
                   'publisheddate',)
