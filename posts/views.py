from django.shortcuts import render
from copy import deepcopy
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from posts.serializers import PostSerializer, LikeSerializer
from posts.models import Post, Like
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.db.utils import IntegrityError


class ListPostsView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            title = request.POST.get('title')
            text = request.POST.get('text')
        except ValueError:
            return Response({'status': 400, 'msg': 'Title or text field does not exists!'})
        try:
            Post.objects.create(body=text, title=title, author=request.user)
        except IntegrityError:
            return Response({'status': 401, 'msg': 'Slug already exists! Change title of the Post!'})
        else:
            return Response({'status': 203, 'msg': 'Post has created already!'})


class DetailsPostsView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, slug):
        obj = get_object_or_404(Post, slug=slug)
        serializer = PostSerializer(obj)
        return Response({'data': serializer.data})


class LikeView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request, slug):
        obj = get_object_or_404(Post, slug=slug)
        user = get_object_or_404(User, username=request.user)
        Like.objects.create(user=user, post=obj)
        return Response({'status': '201'})
