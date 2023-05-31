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
    path('templ/', views.home_page),
    path('admin/', admin.site.urls),
    path('added/', views.success_page),
    path('author_cbv/<int:pk>', views.AuthorView.as_view()),
    path('author/<int:pk>', views.view_Author),
    path('serie/<int:pk>', views.view_Serie),
    path('genre/<int:pk>', views.view_Genre),
    path('publisher/<int:pk>', views.view_Publisher),
    path('author_delete/<int:pk>', views.delete_Author),
    path('serie_delete/<int:pk>', views.delete_Serie),
    path('genre_delete/<int:pk>', views.delete_Genre),
    path('publisher_delete/<int:pk>', views.delete_Publisher),
    path('author_add_cbv/', views.AuthorCreateView.as_view()),
    path('author_upd_cbv/<int:pk>', views.AuthorUpdateView.as_view()),
    path('', views.HomePage.as_view()),
]
