from django.contrib import admin
from .models import Post, Message, Comment, Image, Lesson, Event, Location, Category

class ImageInline(admin.StackedInline):
    model = Image
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'pub_date')
    inlines = [ImageInline]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'content', 'date')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'email', 'date')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'post')
    fieldsets = [(None,               {'fields': ['title']}),
                ('Upload file', {'fields': ['post', 'image']})
    ]

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'youtube')
    fieldsets = [(None,               {'fields': ['title','about']}),
                ('Upload link', {'fields': ['youtube']})
    ]

class EventAdmin(admin.ModelAdmin):
    list_display = ('date', 'description', 'location')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'description')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Location, LocationAdmin)


admin.site.site_header = 'Matinka YOGA'
