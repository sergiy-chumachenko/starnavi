from djoser.serializers import UserCreateSerializer


class UserRegistrationSerializer(UserCreateSerializer):
    class Meta:
        fields = ('username', 'password', 'email')
