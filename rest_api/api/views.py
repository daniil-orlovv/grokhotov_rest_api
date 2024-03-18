from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from api.models import Book, Category, FeedBack
from api.serializers import BookSerializer, CategorySerializer, FeedBackSerializer


class ListRetrieveBook(ReadOnlyModelViewSet):
    """
    Получение всех книг, книг по категории, конкретной книги.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('categories__title',
                        'title',
                        'authors',
                        'status',
                        'publisheddate',)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_detail_request = True
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ListCategory(ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CreateFeedback(CreateAPIView):

    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer
