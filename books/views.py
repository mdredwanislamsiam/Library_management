from rest_framework.viewsets import ModelViewSet
from books.models import Book, BorrowedRecord, Category, Author
from books.serializer import BookSerializer, BorrowedRecordSerializer, AuthorSerializer, CategorySerializer
from django.db.models import Count

class BookViewSet(ModelViewSet): 
    queryset = Book.objects.select_related('category').select_related('author').all()
    serializer_class = BookSerializer 
    
    
    
class CategoryViewSet(ModelViewSet): 
    queryset = Category.objects.annotate(book_count = Count('books')).all()
    serializer_class = CategorySerializer
    
    
    
class AuthorViewSet(ModelViewSet): 
    queryset = Author.objects.annotate(book_count = Count('books')).all()
    serializer_class = AuthorSerializer
    


class BorrowedRecordViewSet(ModelViewSet): 
    queryset = BorrowedRecord.objects.select_related('book').all()
    serializer_class = BorrowedRecordSerializer
    