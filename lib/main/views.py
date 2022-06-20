from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from .models import Author, Book

def home (resquest):
    variables = {
        'books': Book.objects.all(),
        'tablename': [i.name for i in Book._meta.fields]
    }
    return render(resquest,'main/home.html',variables)

def details (resquest,id):
    detail = get_object_or_404 (Book, pk=id)
    variables = {
        'book': detail,
    }
    return render(resquest,'main/detail.html',variables)

