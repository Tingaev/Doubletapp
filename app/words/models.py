from django.db import models
from django.utils.safestring import mark_safe



class Category(models.Model):
    name = models.CharField(max_length=32)
    icon = models.ImageField(upload_to='icon/')

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % self.icon)

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
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % self.photo)

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
        audio = """
        <audio controls>
          <source src="/media/{}" type="audio/mpeg">
          Your browser does not support the audio element.
        </audio>""".format(self.sound)
        return mark_safe(audio)

    def __str__(self):
        return self.name
