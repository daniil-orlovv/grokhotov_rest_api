from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import ListRetrieveBook, ListCategory


router = SimpleRouter()


router.register('books', ListRetrieveBook, basename='books')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/category/', ListCategory.as_view()),
]
