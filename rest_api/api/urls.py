from django.urls import include, path
from rest_framework.routers import SimpleRouter

from views import ListRetrieveBook


router = SimpleRouter()


router.register('books', ListRetrieveBook, basename='onlyread_books')


urlpatterns = [
    path('v1/', include(router.urls)),
]
