from django.urls import path
from App_content import views

app_name = 'App_content'


urlpatterns = [
    path('new-podcast/', views.new_podcast, name='new_podcast'),
    path('pod-showcase/', views.podcast_listview, name='pod-showcase'),
    path('new-post/', views.new_post, name='new-post'),
    path('post-listview/', views.post_listview, name='post-listview'),
    path('love-react/<int:pk>/', views.post_love, name='love-react'),
    path('no-love-react/<int:pk>/', views.post_no_loved, name='no-love-react'),
]