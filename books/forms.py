# book/forms.py

from django.forms import ModelForm
from .models import Book

class AddBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name','author','isbn','notes','image']