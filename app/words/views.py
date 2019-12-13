from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import request, status
from words.models import Category, Level, Theme, Word
from django.http import JsonResponse
from django.conf import settings
from rest_framework import exceptions
from words.serializers import (CategorySerializer,
                               LevelSerializer,
                               ThemeSerializer,
                               ThemeWithWordsSerializer,
                               WordFullSerializer)


def chek_func(function):
    def chek_code(request: request):
        code = request.headers.get('Secret')
        if code == settings.API_SECRET:
            return function(request)
        else:
            # raise exceptions.PermissionDenied('Invalid secret key', code=status.HTTP_403_FORBIDDEN)
            return JsonResponse(data={'error':'Invalid secret key'}, status=status.HTTP_403_FORBIDDEN)
    return chek_code


@chek_func
@api_view(["GET"])
def get_categories(request: request) -> Response:
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@chek_func
@api_view(["GET"])
def get_levels(request: request) -> Response:
    levels = Level.objects.all()
    serializer = LevelSerializer(levels, many=True)
    return Response(serializer.data)

@chek_func
@api_view(["GET"])
def get_themes(request: request) -> Response:
    category = request.GET['category']
    level = request.GET['level']
    themes = Theme.objects.filter(category=category).filter(level=level)
    serializer = ThemeSerializer(themes, many=True)
    return Response(serializer.data)

@chek_func
@api_view(["GET"])
def get_theme(request: request, id: int) -> Response:
    theme = Theme.objects.get(pk=id)
    serializer = ThemeWithWordsSerializer(theme)
    return Response(serializer.data)


@chek_func
@api_view(["GET"])
def get_words(request: request, id: int) -> Response:
    word = Word.objects.get(pk=id)
    serializer = WordFullSerializer(word)
    return Response(serializer.data)
