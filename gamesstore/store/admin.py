from django.contrib import admin
from .models import VideoGame, Gender
# Register your models here.

# class VideogameInLine(admin.StackedInline):
#     model = VideoGame
#     extra = 3

class VideogameInLine(admin.TabularInline):
    model = VideoGame
    extra = 3

class VideoGameAdmin(admin.ModelAdmin):
    # fields = ['name', 'gender', 'on_stock', 'score']
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Availability', {'fields': ['on_stock', 'score']}),
    ]
    list_display = ['name','gender','on_stock']
    list_filter = ['gender']
    search_fields = ['name']

class GenderAdmin(admin.ModelAdmin):
    inlines = [VideogameInLine]


admin.site.register(VideoGame, VideoGameAdmin)
admin.site.register(Gender)