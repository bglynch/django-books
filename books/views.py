from django.shortcuts import render, redirect
from .models import Book
from .forms import AddBookForm
from django.http import HttpResponse

# Create your views here.
def get_index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

def add_book(request):
    if request.method == "POST":
        add_book_form = AddBookForm(request.POST, request.FILES)
        if add_book_form.is_valid():
            add_book_form.save()
        return redirect('/')
    else:
        add_book_form = AddBookForm()
    
    return render(request, 'books/addbook.html', {'form': add_book_form})
