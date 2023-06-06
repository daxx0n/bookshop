from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name="Home Page"),
    path('success/', views.success_page, name="Success Page"),
    path('authors_list_view/', views.AuthorListView.as_view(), name="Authors list"),
    path('genres_list_view/', views.GenreListView.as_view(), name="Genres list"),
    path('publishers_list_view/', views.PublisherListView.as_view(), name="Publishers List"),
    path('series_list_view/', views.SerieListView.as_view(), name="Series List"),
    #Read
    path('author_view/<int:pk>', views.AuthorView.as_view(), name="Author View"),
    path('serie_view/<int:pk>', views.SerieView.as_view(), name="Serie View"),
    path('genre_view/<int:pk>', views.GenreView.as_view(), name="Genre View"),
    path('publisher_view/<int:pk>', views.PublisherView.as_view(), name="Publisher View"),
    #Delete
    path('author_delete/<int:pk>', views.AuthorDeleteView.as_view(), name="Author Delete"),
    path('serie_delete/<int:pk>', views.SerieDeleteView.as_view(), name="Serie Delete"),
    path('genre_delete/<int:pk>', views.GenreDeleteView.as_view(), name="Genre Delete"),
    path('publisher_delete/<int:pk>', views.PublisherDeleteView.as_view(), name="Publisher Delete"),
    #Create
    path('author_add/', views.AuthorCreateView.as_view(), name="Author Add"),
    path('serie_add/', views.SerieCreateView.as_view(), name="Serie Add"),
    path('genre_add/', views.GenreCreateView.as_view(), name="Genre Add"),
    path('publisher_add/', views.PublisherCreateView.as_view(), name="Publisher Add"),
    #Update
    path('author_upd/<int:pk>', views.AuthorUpdateView.as_view(), name="Author Update"),
    path('serie_upd/<int:pk>', views.SerieUpdateView.as_view(), name="Serie Update"),
    path('genre_upd/<int:pk>', views.GenreUpdateView.as_view(), name="Genre Update"),
    path('publisher_upd/<int:pk>', views.PublisherUpdateView.as_view(), name="Publisher Update"),
]