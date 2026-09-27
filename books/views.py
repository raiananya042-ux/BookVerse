from django.db import models
from django.shortcuts import get_object_or_404, render
from .models import Book

def home(request):
    books = Book.objects.all()
    query = request.GET.get("q", "").strip()
    genre = request.GET.get("genre", "").strip()

    if query:
        books = books.filter(
            models.Q(title__icontains=query) |
            models.Q(author__icontains=query) |
            models.Q(genre__icontains=query) |
            models.Q(description__icontains=query) |
            models.Q(themes__icontains=query)
        )

    if genre:
        books = books.filter(genre=genre)

    genres = Book.objects.values_list("genre", flat=True).distinct().order_by("genre")
    return render(request, "books/home.html", {
        "books": books,
        "genres": genres,
        "query": query,
        "selected_genre": genre,
    })

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/book_detail.html", {"book": book})

def bookverse(request):
    return render(request, "books/BookVerse.html")
