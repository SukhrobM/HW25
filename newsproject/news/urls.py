from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('articles/<int:pk>', views.get_articles),
    path('categories/<int:pk>', views.get_category),
    path('search', views.search_article)
]
