from books.models import Book, Category, BorrowedRecord, Author
from users.models import User 
from rest_framework import serializers






class CategorySerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Category
        fields = ['id', 'name', 'description', 'book_count']
    book_count = serializers.IntegerField(read_only = True)
    
    
    
    
class AuthorSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Author 
        fields = ['id', 'name', 'biography', 'book_count']
    book_count = serializers.IntegerField(read_only = True)




class BorrowedRecordSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = BorrowedRecord
        fields = ['id', 'book', 'member', 'borrow_date', 'return_date']
        read_only_fields = ['member']
        
    def create(self, validated_data):
        validated_data['member'] = self.context['request'].user
        return super().create(validated_data)

    


class BookSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Book
        fields = ['id', 'title', 'author', 'category', 'isbn', 'available_status']
    