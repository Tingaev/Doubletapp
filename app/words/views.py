from rest_framework import generics
from rest_framework.exceptions import NotFound


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
    mdoel = Theme
    serializer_class = ThemeSerializer

    def get_queryset(self):
        queryset = Theme.objects.all()
        category = self.request.query_params.get('category')
        level = self.request.query_params.get('level')

        if category:
            queryset = queryset.filter(category=category)
        elif level:
            queryset = queryset.filter(level=level)

        if queryset:
            return queryset
        raise NotFound()





class ThemeDetail(generics.RetrieveAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeWithWordsSerializer


class WordDetail(generics.RetrieveAPIView):
    queryset = Word.objects.all()
    serializer_class = WordFullSerializer
