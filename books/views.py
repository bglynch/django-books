from django.shortcuts import render, redirect
from .models import Book
from .forms import AddBookForm
from django.http import HttpResponse

# Create your views here.
def get_index(request):
    if request.user.is_authenticated:
        books = Book.objects.filter(owner=request.user)
    else:
        books = []
    return render(request, 'index.html', {'books': books})

def add_book(request):
    if request.method == "POST":
        add_book_form = AddBookForm(request.POST, request.FILES)
        if add_book_form.is_valid():
            book = add_book_form.save(commit=False)
            book.owner = request.user
            book.save()
        return redirect('/')
    else:
        add_book_form = AddBookForm()
    
    return render(request, 'books/addbook.html', {'form': add_book_form})
