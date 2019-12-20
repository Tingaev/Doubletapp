from django.db import models
from django.template.loader import render_to_string



class Category(models.Model):
    name = models.CharField(max_length=32)
    icon = models.ImageField(upload_to='icon/')

    def image_tag(self):
        return render_to_string('image_temp.html', {'link': self.icon})

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Theme(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    photo = models.ImageField(upload_to='photo/')

    def image_tag(self):
        return render_to_string('image_temp.html', {'link': self.photo})

    def __str__(self):
        return self.name


class Word(models.Model):
    name = models.CharField(max_length=64)
    translation = models.CharField(max_length=64)
    transcription = models.CharField(max_length=64)
    example = models.TextField()
    sound = models.FileField(upload_to='sound/')
    theme = models.ForeignKey(Theme, related_name='words', on_delete=models.CASCADE)

    def audio_tag(self):
        return render_to_string('audio_play.html', {'link': self.sound})

    def __str__(self):
        return self.name
