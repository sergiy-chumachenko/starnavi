from django.urls import path
from posts.views import ListPostsView, DetailsPostsView, LikeView

urlpatterns = [
    path('posts/', ListPostsView.as_view()),
    path('posts/<str:slug>', DetailsPostsView.as_view()),
    path('posts/<str:slug>/like/', LikeView.as_view())
]