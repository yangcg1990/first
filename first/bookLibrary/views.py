from django.shortcuts import render

from django.views.generic import ListView
from bookLibrary.models import Book, Author


# Create your views here.
class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'bookLibrary/book/list.html'
