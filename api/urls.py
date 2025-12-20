from rest_framework.routers import DefaultRouter
from books.views import BookViewSet, BorrowedRecordViewSet, CategoryViewSet, AuthorViewSet
from users.views import UserViewSet

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('categories', CategoryViewSet)
router.register('authors', AuthorViewSet)
router.register('borrowed_records', BorrowedRecordViewSet)
router.register('user', UserViewSet)


urlpatterns = router.urls
