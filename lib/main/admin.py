from django.contrib import admin

from .models import Author, Book
# Register your models here.

class AuthorDisplay(admin.ModelAdmin):
    list_display = ('id','name')

class BookDisplay(admin.ModelAdmin):
    list_display = ('id','title','author','release_year')


admin.site.register(Author,AuthorDisplay)
admin.site.register(Book,BookDisplay)