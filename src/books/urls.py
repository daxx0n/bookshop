from django.urls import path
from books import views
app_name = 'books'

urlpatterns = [
    path('book_list_view/', views.BookListView.as_view(), name="book_list"),
    path('book_view/<int:pk>', views.BookView.as_view(), name="book_view"),
    path('book_delete/<int:pk>', views.BookDeleteView.as_view(), name="book_delete"),
    path('book_add/', views.BookCreateView.as_view(), name="book_add"),
    path('book_upd/<int:pk>', views.BookUpdateView.as_view(), name="book_update"),
    # COMMENTS
    path('book/<int:comment_id>/comment/', views.add_comment, name='add_comment'),
]