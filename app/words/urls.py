from django.urls import path
from words.views import ThemesList, WordDetail, ThemeDetail, LevelsList, CategoriesList


urlpatterns = [
    path('categories', CategoriesList.as_view(), name='get_categories'),
    path('themes', ThemesList.as_view(), name='get_themes'),
    path('levels', LevelsList.as_view(), name='get_levels'),
    path('themes/<int:pk>', ThemeDetail.as_view(), name='get_theme'),
    path('words/<int:pk>', WordDetail.as_view(), name='get_words'),
]
