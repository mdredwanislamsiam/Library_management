from rest_framework.viewsets import ModelViewSet
from books.models import Book, BorrowedRecord, Category, Author
from books.serializer import BookSerializer, BorrowedRecordSerializer, AuthorSerializer, CategorySerializer
from django.db.models import Count
from rest_framework.permissions import DjangoModelPermissions
from drf_yasg.utils import swagger_auto_schema


class BookViewSet(ModelViewSet):
    queryset = Book.objects.select_related('category', 'author').all()
    serializer_class = BookSerializer
    permission_classes = [DjangoModelPermissions]

    @swagger_auto_schema(
        operation_summary="List books",
        operation_description="Retrieve a list of all books with category and author details",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve book",
        operation_description="Retrieve a single book by ID",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create book",
        operation_description="Create a new book record",
        request_body=BookSerializer,
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update book",
        operation_description="Update all fields of a book",
        request_body=BookSerializer,
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update book",
        operation_description="Update one or more fields of a book",
        request_body=BookSerializer,
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete book",
        operation_description="Delete a book by ID",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(book_count=Count('books')).all()
    serializer_class = CategorySerializer
    permission_classes = [DjangoModelPermissions]

    @swagger_auto_schema(
        operation_summary="List categories",
        operation_description="Retrieve all categories with book count",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve category",
        operation_description="Retrieve a single category",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create category",
        operation_description="Create a new category",
        request_body=CategorySerializer,
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update category",
        operation_description="Update a category",
        request_body=CategorySerializer,
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Partially update category",
        operation_description="Update one or more fields of a category",
        request_body=BookSerializer,
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete category",
        operation_description="Delete a category",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.annotate(book_count=Count('books')).all()
    serializer_class = AuthorSerializer
    permission_classes = [DjangoModelPermissions]

    @swagger_auto_schema(
        operation_summary="List authors",
        operation_description="Retrieve all authors with book count",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve author",
        operation_description="Retrieve a single author",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create author",
        operation_description="Create a new author",
        request_body=AuthorSerializer,
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Update author",
        operation_description="Update all fields of an author",
        request_body=BookSerializer,
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update author",
        operation_description="Update one or more fields of an author",
        request_body=BookSerializer,
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete author",
        operation_description="Delete an author",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class BorrowedRecordViewSet(ModelViewSet):
    serializer_class = BorrowedRecordSerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return BorrowedRecord.objects.none
        queryset = BorrowedRecord.objects.select_related('book').all()
        if not self.request.user.is_staff:
            queryset = queryset.filter(member=self.request.user)
        return queryset


    @swagger_auto_schema(
        operation_summary="List borrowed records",
        operation_description=(
            "Retrieve borrowed records. "
            "Staff users see all records; normal users see only their own."
        ),
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Borrow a book",
        operation_description="Create a borrowed record",
        request_body=BorrowedRecordSerializer,
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a borrowed record",
        operation_description="Retrieve a single borrowed record by ID",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Update borrowed record",
        operation_description="Update all fields of a borrowed record",
        request_body=BookSerializer,
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update borrowed record",
        operation_description="Update one or more fields of a borrowed record",
        request_body=BookSerializer,
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Return / delete borrowed record",
        operation_description="Delete a borrowed record",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
