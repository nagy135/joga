from django.shortcuts import render, redirect
from .models import Post, Image, Lesson, Event, Location
from .forms import NameForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.conf import settings

import os

def index(request):
    data = dict()
    data['css'] = 'index.css'
    data['js'] = 'index.js'
    return render(request, 'joga_app/index.html', data)

def blog(request):
    data = dict()
    posts = Post.objects.all().filter(category__id=1).order_by('-pub_date')
    offset = 0
    limit = offset + settings.MAX_POSTS
    if limit >= posts.count():
        limit = posts.count()

    posts = posts[offset:limit]

    max_len = 1000
    for post in posts:
        image_query = Image.objects.all().filter(post=post)
        post.images = list()
        for image in image_query:
            image_name = os.path.basename(image.image.url)
            post.images.append(image_name)
        if len(post.content) > max_len:
            post.content = post.content[0:max_len]
    data = dict()
    data['posts'] = posts
    if not request.POST.get('resupply', False):
        data['css'] = 'blog.css'
        data['js'] = 'blog.js'
        data['post_count'] = limit;
        return render(request, 'joga_app/blog.html', data)
    else:
        return render(request, 'joga_app/post_item.html', data)

def submit_comment(request):
    return JsonResponse({'success': True})

def post(request, post_id=None):
    if post_id is None:
        return HttpResponseRedirect(reverse( 'joga_app:index' ))
    posts = Post.objects.filter(id=post_id)
    for post in posts:
        image_query = Image.objects.all().filter(post=post)
        post.images = list()
        for image in image_query:
            image_name = os.path.basename(image.image.url)
            post.images.append(image_name)
    post = posts[0]
    data = dict()
    data['css'] = 'post.css'
    data['js'] = 'post.js'
    data['post'] = post
    return render(request, 'joga_app/post.html', data)

def lessons(request):
    lessons = Lesson.objects.all()
    data = dict()
    data['lessons'] = lessons
    for lesson in lessons:
        lesson.youtube = lesson.youtube.replace('watch?v=', 'embed/')
    data['css'] = 'lessons.css'
    data['js'] = 'lessons.js'
    return render(request, 'joga_app/lessons.html', data)

def events(request):
    events = Event.objects.all()
    print('events', events)
    data = dict()
    data['events'] = events
    data['css'] = 'events.css'
    data['js'] = 'events.js'
    return render(request, 'joga_app/events.html', data)

def location(request, location_id=None):
    if location_id is None:
        return HttpResponseRedirect(reverse( 'joga_app:events' ))
    locations = Location.objects.filter(id=location_id)
    location = locations[0]
    if location.image:
        location.image_url = os.path.basename(location.image.url)
    data = dict()
    data['css'] = 'location.css'
    data['js'] = 'location.js'
    data['location'] = location
    return render(request, 'joga_app/location.html', data)

def lesson(request, lesson_id=None):
    if lesson_id is None:
        return HttpResponseRedirect(reverse( 'joga_app:lessons' ))
    lessons = Lesson.objects.filter(id=lesson_id)
    lesson = lessons[0]
    lesson.youtube = lesson.youtube.replace('watch?v=', 'embed/')
    data = dict()
    data['css'] = 'lesson.css'
    data['js'] = 'lesson.js'
    data['lesson'] = lesson
    return render(request, 'joga_app/lesson.html', data)

def recipes(request):
    data = dict()
    posts = Post.objects.all().filter(category__id=2).order_by('-pub_date')
    offset = 0
    limit = offset + 5
    if limit >= posts.count():
        limit = posts.count()

    posts = posts[offset:limit]

    max_len = 1000
    for post in posts:
        image_query = Image.objects.all().filter(post=post)
        post.images = list()
        for image in image_query:
            image_name = os.path.basename(image.image.url)
            post.images.append(image_name)
        if len(post.content) > max_len:
            post.content = post.content[0:max_len]
        post.images = post.images[:1]
    data['posts'] = posts
    data['css'] = 'recipes.css'
    data['js'] = 'recipes.js'
    return render(request, 'joga_app/recipes.html', data)

def about_me(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print(form.cleaned_data)
            # redirect to a new URL:
            return HttpResponseRedirect(reverse( 'joga_app:index' ))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    data = dict()
    data['css'] = 'about_me.css'
    data['js'] = 'about_me.js'
    data['form'] = form
    return render(request, 'joga_app/about_me.html', data)
