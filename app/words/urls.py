from django.urls import path
from words.views import get_categories, get_themes, get_theme, get_words, get_levels


urlpatterns = [
    path('categories', get_categories, name='get_categories'),
    path('themes', get_themes, name='get_themes'),
    path('levels', get_levels, name='get_levels'),
    path('themes/<int:id>', get_theme, name='get_theme'),
    path('words/<int:id>', get_words, name='get_words'),
]
