from django.db import models
import datetime
from django.contrib import admin
import os
from django.conf import settings

class Location(models.Model):
    name = models.CharField(max_length=200, blank=False)
    latitude = models.FloatField(blank=False, default=0)
    longitude = models.FloatField(blank=False, default=0)
    description = models.TextField(max_length=20000, default='To Do', null=True)
    image = models.ImageField(default=None, upload_to='joga_app/static/joga_app/locationImages/', null=True )
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

class Event(models.Model):
    date = models.DateTimeField()
    description = models.TextField(max_length=20000, default='To Do', null=True)
    location = models.ForeignKey(Location, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.location.name + " " + str(self.date)
    def __unicode__(self):
        return self.location.name + " " + str(self.date)

class Category(models.Model):
    name = models.CharField(max_length=200, blank=False)
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(max_length=20000, default='To Do', null=True)
    pub_date = models.DateTimeField('date published')
    category = models.ForeignKey(Category, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    def publishDate(self):
        return self.pub_date

class Image(models.Model):
    title = models.CharField(max_length=200, blank=False)
    post = models.ForeignKey(Post, blank=False, on_delete=models.CASCADE)
    image = models.ImageField(default=None, upload_to='joga_app/static/joga_app/postImages/' )

    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)
        initial_path = self.image.path
        new_path = os.path.join(settings.BASE_DIR, 'joga_app', 'static', 'joga_app', 'postImages', str(self.post.id) ,os.path.basename(initial_path))
        if not os.path.exists(os.path.dirname(new_path)):
            os.makedirs(os.path.dirname(new_path))

        os.rename(initial_path, new_path)

class Message(models.Model):
    name = models.CharField(max_length=200, blank=False)
    content = models.TextField(max_length=21000, blank=False)
    email = models.CharField(max_length=248)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + '/' + self.name

    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    title = models.CharField(max_length=200, blank=False)
    about = models.TextField(max_length=20000)
    youtube = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return 'Lesson : ' +  str(self.id) + ' | ' + self.title

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, blank=False, on_delete=models.CASCADE)
    user = models.CharField(max_length=300, blank=False)
    content = models.TextField(max_length=3000, blank=False)
    date = models.DateField(auto_now_add=True)
