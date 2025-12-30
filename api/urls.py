from rest_framework.routers import DefaultRouter
from books.views import BookViewSet, BorrowedRecordViewSet, CategoryViewSet, AuthorViewSet
from users.views import UserViewSet
from django.urls import path, include
router = DefaultRouter()
router.register('books', BookViewSet)
router.register('categories', CategoryViewSet)
router.register('authors', AuthorViewSet)
router.register('borrowed_records', BorrowedRecordViewSet, basename='borrowed-record')

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += router.urls
