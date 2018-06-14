from django.shortcuts import render
from .models import Book

# Create your views here.
def get_index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

def add_book(request):
    return render(request, 'books/addbook.html', {})
