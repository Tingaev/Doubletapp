from django.contrib import admin
from words.models import Category, Level, Theme, Word

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'icon', 'image_tag')
    fields = ('name', 'icon','image_tag')
    readonly_fields = ('image_tag',)


class ThemeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'photo', 'image_tag')
    fields = ('category', 'level', 'name', 'photo', 'image_tag')
    readonly_fields = ('image_tag',)


class WordAdmin(admin.ModelAdmin):
    list_display = ('pk', 'audio_tag')

    fields = ('translation', 'transcription', 'example', 'sound', 'audio_tag')
    readonly_fields = ('audio_tag',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Word, WordAdmin)

admin.site.register(Level)
admin.site.register(Theme, ThemeAdmin)

