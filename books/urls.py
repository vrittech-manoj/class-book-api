from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .viewset import BooksViewsets

router = DefaultRouter()

router.register('books',BooksViewsets,basename='BooksViewsets')


urlpatterns = [
    path("", include(router.urls)),
]
