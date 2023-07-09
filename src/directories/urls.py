from django.urls import path
from . import views
app_name = 'directories'

urlpatterns = [
    # path('success/', views.success_page, name="Success_Page"),
    path('authors_list_view/', views.AuthorListView.as_view(), name="authors_list"),
    path('genres_list_view/', views.GenreListView.as_view(), name= "genres_list"),
    path('publishers_list_view/', views.PublisherListView.as_view(), name="publishers_list"),
    path('series_list_view/', views.SerieListView.as_view(), name="series_list"),
    #Read
    path('author_view/<int:pk>', views.AuthorView.as_view(), name="author_view"),
    path('serie_view/<int:pk>', views.SerieView.as_view(), name="serie_view"),
    path('genre_view/<int:pk>', views.GenreView.as_view(), name="genre_view"),
    path('publisher_view/<int:pk>', views.PublisherView.as_view(), name="publisher_view"),
    #Delete
    path('author_delete/<int:pk>', views.AuthorDeleteView.as_view(), name="author_delete"),
    path('serie_delete/<int:pk>', views.SerieDeleteView.as_view(), name="serie_delete"),
    path('genre_delete/<int:pk>', views.GenreDeleteView.as_view(), name="genre_delete"),
    path('publisher_delete/<int:pk>', views.PublisherDeleteView.as_view(), name="publisher_delete"),
    #Create
    path('author_add/', views.AuthorCreateView.as_view(), name="author_add"),
    path('serie_add/', views.SerieCreateView.as_view(), name="serie_add"),
    path('genre_add/', views.GenreCreateView.as_view(), name="genre_add"),
    path('publisher_add/', views.PublisherCreateView.as_view(), name="publisher_add"),
    #Update
    path('author_upd/<int:pk>', views.AuthorUpdateView.as_view(), name="author_update"),
    path('serie_upd/<int:pk>', views.SerieUpdateView.as_view(), name="serie_update"),
    path('genre_upd/<int:pk>', views.GenreUpdateView.as_view(), name="genre_update"),
    path('publisher_upd/<int:pk>', views.PublisherUpdateView.as_view(), name="publisher_update"),
]