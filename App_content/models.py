from django.db import models
from App_auth.models import *


# Create your models here.
class PodcastModel(models.Model):
    host = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='podcast_creator')
    title = models.CharField(max_length=800)
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='podcast_images', blank=True, null=True)
    audio_file = models.FileField(upload_to='music/', blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_on']


class PodcastLoveReact(models.Model):
    post = models.ForeignKey(PodcastModel, on_delete=models.CASCADE, related_name='liked_podcast')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='podcast_liker')
    date_created = models.DateTimeField(auto_now_add=True)

    def str(self):
        return "{} : {}".format(self.user, self.post)


class PostsModel(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='resource_sharing')
    topic_name = models.CharField(max_length=100)
    post_image1 = models.ImageField(upload_to='post_images', blank=True, null=True)
    post_image2 = models.ImageField(upload_to='post_images', blank=True, null=True)
    post_image3 = models.ImageField(upload_to='post_images', blank=True, null=True)
    my_text = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_on"]

    def str(self):
        return self.topic_name


class PostLoveReact(models.Model):
    post = models.ForeignKey(PostsModel, on_delete=models.CASCADE, related_name='liked_post')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='post_liker')
    date_created = models.DateTimeField(auto_now_add=True)

    def str(self):
        return "{} : {}".format(self.user, self.post)
