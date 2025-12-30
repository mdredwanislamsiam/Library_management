from django.contrib import admin
from books.models import Book, Category, BorrowedRecord, Author


admin.site.register(Book)
admin.site.register(Category)
admin.site.register(BorrowedRecord)
admin.site.register(Author)