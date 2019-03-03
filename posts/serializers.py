from rest_framework.serializers import ModelSerializer, SerializerMethodField
from posts.models import Post, Like
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class LikeSerializer(ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


class PostSerializer(ModelSerializer):
    author = UserSerializer()
    likes = SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_likes(self, obj):
        return obj.likes.count()




