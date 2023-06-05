"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from directories import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name="Home Page"),
    path('success/', views.success_page, name="Success Page"),
    path('authors_list_view/', views.AuthorListView.as_view()),
    path('genres_list_view/', views.GenreListView.as_view()),
    path('publishers_list_view/', views.PublisherListView.as_view()),
    path('series_list_view/', views.SerieListView.as_view()),
    #Read
    path('author_view/<int:pk>', views.AuthorView.as_view()),
    path('serie_view/<int:pk>', views.SerieView.as_view()),
    path('genre_view/<int:pk>', views.GenreView.as_view()),
    path('publisher_view/<int:pk>', views.PublisherView.as_view()),
    #Delete
    path('author_delete/<int:pk>', views.AuthorDeleteView.as_view()),
    path('serie_delete/<int:pk>', views.SerieDeleteView.as_view()),
    path('genre_delete/<int:pk>', views.GenreDeleteView.as_view()),
    path('publisher_delete/<int:pk>', views.PublisherDeleteView.as_view()),
    #Create
    path('author_add/', views.AuthorCreateView.as_view()),
    path('serie_add/', views.SerieCreateView.as_view()),
    path('genre_add/', views.GenreCreateView.as_view()),
    path('publisher_add/', views.PublisherCreateView.as_view()),
    #Update
    path('author_upd/<int:pk>', views.AuthorUpdateView.as_view()),
    path('serie_upd/<int:pk>', views.SerieUpdateView.as_view()),
    path('genre_upd/<int:pk>', views.GenreUpdateView.as_view()),
    path('publisher_upd/<int:pk>', views.PublisherUpdateView.as_view()),
]
