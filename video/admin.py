from django.contrib import admin
from video.models import Video


class VideoModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'url')
    search_fields = ('title',)
    
admin.site.register(Video, VideoModelAdmin)