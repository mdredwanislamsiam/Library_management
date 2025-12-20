from django.db import models
from users.models import User


class Category(models.Model): 
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self): 
        return self.name
    


class Author(models.Model): 
    name = models.CharField(max_length=100)
    biography = models.TextField()
    def __str__(self):
        return self.name



class Book(models.Model): 
    AVAILABLE = 'Available'
    BORROWED = 'Borrowed'
    NOT_AVAILABLE = 'Not_available'
    STATUS_CHOICES = [
        (AVAILABLE, 'Available'), 
        (BORROWED, 'Borrowed'), 
        (NOT_AVAILABLE, 'Not_available'), 
    ]
    title  = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=13)
    available_status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=AVAILABLE)
    
    def __str__(self):
        return self.title
    
    
    
class BorrowedRecord(models.Model): 
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrowed_record')
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowed_record')
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null = True, blank=True)
    
    class Meta: 
        constraints  = [
            models.UniqueConstraint(
                fields=['book'], 
                condition=models.Q(return_date__isnull = True), 
                name = 'one_active_borrow_per_book'
            )
        ]
    
    def __str__(self):
        return f"{self.book} -> {self.member}"