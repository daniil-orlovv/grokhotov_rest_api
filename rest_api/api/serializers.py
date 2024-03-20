from rest_framework import serializers

from api.models import (Book, Category, SubCategory, FeedBack, Author)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'title',
        )


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = (
            'title',
        )


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
            'name'
        )


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer(
        many=True,
        source='categories',
        read_only=True
    )
    authors = AuthorSerializer(
        many=True,
        read_only=True
    )
    related_books = serializers.SerializerMethodField(
        method_name='get_related_books'
    )
    subcategory = SubCategorySerializer(
        many=True,
        source='subcategories',
        read_only=True
    )

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'isbn',
            'pagecount',
            'publisheddate',
            'thumbnailurl',
            'status',
            'authors',
            'category',
            'subcategory',
            'related_books'
        )

    def get_related_books(self, obj):
        if hasattr(obj, 'is_detail_request') and obj.is_detail_request:
            category = obj.categories.first()
            related_books = Book.objects.filter(
                categories=category).exclude(
                    id=obj.id).order_by('-publisheddate')[:5]
            serializer = self.__class__(related_books, many=True)
            return serializer.data
        return None


class FeedBackSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeedBack
        fields = (
            'id',
            'email',
            'name',
            'comment',
            'phone',
        )
