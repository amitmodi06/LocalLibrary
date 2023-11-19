from django.contrib import admin
from .models import Book, Author, Genre,  BookInstance, Language

# Register your models here.

"""Minimal registration of Models.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
"""

admin.site.register(Genre)
admin.site.register(Language)


@admin.register(Book)  # this decorator is another way of writing admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')


@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')


# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'data_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth', 'data_of_death')]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

