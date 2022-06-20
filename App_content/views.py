from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from App_content.models import *


# Create your views here.

@login_required
def new_podcast(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        cover_image = request.FILES.get('cover_image')
        audio_file = request.FILES.get('podcastFile')
        description = request.POST.get('description')
        audio_model = PodcastModel(host=request.user, title=title, description=description, cover_image=cover_image,
                                   audio_file=audio_file)
        audio_model.save()
        return HttpResponseRedirect(reverse('home'))
    return HttpResponseRedirect(reverse('home'))


@login_required
def podcast_listview(request):
    pod_list = PodcastModel.objects.filter(status=True)
    content = {
        'pod_list': pod_list,
    }
    return render(request, 'App_content/podcast_listview.html', context=content)


@login_required
def new_post(request):
    if request.method == 'POST':
        post_title = request.POST.get('topic_name')
        my_content = request.POST.get('my-content')
        image1 = request.FILES.get('image_1')
        image2 = request.FILES.get('image_2')
        image3 = request.FILES.get('image_3')

        post_model = PostsModel(author=request.user, topic_name=post_title, post_image1=image1, post_image2=image2,
                                post_image3=image3, my_text=my_content, status=True)
        post_model.save()
        return HttpResponseRedirect(reverse('home'))
    return HttpResponseRedirect(reverse('home'))


@login_required
def post_listview(request):
    post_list = PostsModel.objects.filter(status=True)
    content = {
        'post_list': post_list,
    }
    return render(request, 'App_content/post_listview.html', context=content)


@login_required
def post_love(request, pk):
    post = get_object_or_404(PostsModel, id=pk)
    print(post)
    already_loved = PostLoveReact.objects.filter(post=post, user=request.user)
    if not already_loved.exists():
        print("not exist")
        like_post = PostLoveReact(post=post, user=request.user)
        like_post.save()
        return HttpResponseRedirect(reverse('home'))


@login_required
def post_no_loved(request, pk):
    post = PostsModel.objects.get(id=pk)
    print(post)
    already_loved = PostLoveReact.objects.filter(post=post, user=request.user)
    print(already_loved)
    already_loved.delete()
    return HttpResponseRedirect(reverse('home'))
