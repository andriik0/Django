from django.db.models import Q
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book

    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'


class SearchResultsView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self) -> QuerySet:
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
