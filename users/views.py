from users.serializers import UserCreateSerializer
from users.utils import get_additional_info, check_email

from posts.serializers import UserSerializer

from starnavi_task.settings import HUNTER_IS_ACTIVE

from rest_framework.response import Response
from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet

from django.contrib.auth.models import User


class UserViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        user_email = request.POST.get('email')
        serializer = UserCreateSerializer(data=request.POST)
        email_is_valid = check_email(user_email) if HUNTER_IS_ACTIVE else True
        if not email_is_valid:
            return Response(status=400,
                            data={'msg': 'Email is not valid for instance. Use valid company domain instead!'})
        if serializer.is_valid():
            serializer.save()
            additional_info = get_additional_info(user_email)
            if additional_info is not None and additional_info.get('data') is not None:
                user = User.objects.get(email=user_email)
                first_name, last_name = str(additional_info.get('data')).split()
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                return Response(status=201, data={'additional_info': 1,
                                                  'msg': 'User has created with additional info!'})
            else:
                return Response(status=201, data={'additional_info': 0,
                                                  'msg': 'User has created without additional info!'})
        else:
            return Response(status=400, data={'msg': 'Error! User has not created!'})

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [permissions.AllowAny, ]
        else:
            permission_classes = [permissions.IsAuthenticated, ]
        return [permission() for permission in permission_classes]
