from django.urls import include, path
from .views import CreatePostAPIView, ListPostAPIView, DetailPostAPIView, PostLikeAPIView

app_name = 'forum_api'

urlpatterns = [
    path("", ListPostAPIView.as_view(), name="list_post"),
    path('posts/create', CreatePostAPIView.as_view(), name="create_post"),
    path("<str:slug>/", DetailPostAPIView.as_view(), name="post_detail"),
    path("<str:slug>/like/", PostLikeAPIView.as_view(), name="like_post"),
]