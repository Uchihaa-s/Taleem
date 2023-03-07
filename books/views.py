from django.shortcuts import render
from django.views.generic import ListView

from books.models import Books_model


class BookListView(ListView):
    template_name = "books.html"
    model = Books_model
