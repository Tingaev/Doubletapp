from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


from words.models import Category, Level, Theme, Word
from words.serializers import (CategorySerializer,
                               LevelSerializer,
                               ThemeSerializer,
                               ThemeWithWordsSerializer,
                               WordFullSerializer)



class CategoriesList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LevelsList(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ThemesList(generics.ListAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'level']


class ThemeDetail(generics.RetrieveAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeWithWordsSerializer


class WordDetail(generics.RetrieveAPIView):
    queryset = Word.objects.all()
    serializer_class = WordFullSerializer
