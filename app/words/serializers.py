from rest_framework import serializers
from words.models import Category, Level, Theme, Word


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name', 'icon']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['pk', 'name', 'code']


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('pk', 'category', 'level', 'name', 'photo',)


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('pk', 'name')


class WordFullSerializer(WordSerializer):
    class Meta(WordSerializer.Meta):
        fields = WordSerializer.Meta.fields + ('translation', 'transcription', 'example', 'sound')


class ThemeWithWordsSerializer(ThemeSerializer):
    words = WordSerializer(many=True, read_only=True)

    class Meta(ThemeSerializer.Meta):
        fields = ThemeSerializer.Meta.fields + ('words',)