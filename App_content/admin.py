from django.contrib import admin
from App_content.models import *

# Register your models here.
admin.site.register(PodcastModel)
admin.site.register(PostsModel)
admin.site.register(PodcastLoveReact)
admin.site.register(PostLoveReact)
