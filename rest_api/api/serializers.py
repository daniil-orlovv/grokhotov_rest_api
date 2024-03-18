from rest_framework import serializers

from api.models import Book, Category, FeedBack, Author


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
        )


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(
        many=True,
        source='category_subcategories',
        read_only=True
    )

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'subcategories'
        )


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
            'name'
        )


class BookSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(
        many=True,
        read_only=True
    )
    authors = AuthorSerializer(
        many=True,
        read_only=True
    )
    related_books = serializers.SerializerMethodField(
        method_name='get_related_books'
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
            'categories',
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
    ...
