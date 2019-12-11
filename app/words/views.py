from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import request
from words.models import Category, Level, Theme, Word

from words.serializers import (CategorySerializer,
                               LevelSerializer,
                               ThemeSerializer,
                               ThemeWithWordsSerializer,
                               WordFullSerializer)


@api_view(["GET"])
def get_categories(request: request) -> Response:
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_levels(request: request) -> Response:
    levels = Level.objects.all()
    serializer = LevelSerializer(levels, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_themes(request: request) -> Response:
    themes = Theme.objects.all()
    serializer = ThemeSerializer(themes, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_theme(request: request, id: int) -> Response:
    theme = Theme.objects.get(pk=id)
    serializer = ThemeWithWordsSerializer(theme)
    return Response(serializer.data)


@api_view(["GET"])
def get_words(request: request, id: int) -> Response:
    word = Word.objects.get(pk=id)
    serializer = WordFullSerializer(word)
    return Response(serializer.data)
