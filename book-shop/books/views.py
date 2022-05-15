from django.shortcuts import render
from django.views.generic import ListView , DetailView , TemplateView
from .models import Book

class BookListView(ListView):
    template_name = 'book_list.html'
    model= Book
    context_object_name = 'book_list'

class BookDetailView(DetailView):
    template_name = 'book_detail.html'
    model = Book

class BookTemplateView(TemplateView):
    template_name = 'book_template.html'
    
