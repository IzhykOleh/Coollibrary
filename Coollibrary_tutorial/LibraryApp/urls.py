from django.conf.urls import include
from django.urls import path
from LibraryApp.views import index
import LibraryApp.views as views

urlpatterns = [
    path('', index, name="index"),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]
