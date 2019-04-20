from django.contrib.auth.models import User
from rest_framework import serializers, status
from userProfile.models import UserProfile
from basic.models import Tusa


class UserSerializer(serializers.ModelSerializer):
    userprofile_url = serializers.HyperlinkedIdentityField(
        view_name='userprofile-detail')
    class Meta:
        depth = 1
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 'email',
                  'is_superuser', 'is_staff', 'userprofile', 'userprofile_url')

class UserProfileSerializer(serializers.ModelSerializer):
    user_url = serializers.HyperlinkedIdentityField(view_name='user-detail')
    user = serializers.ReadOnlyField(source='user.id')
    id = serializers.IntegerField(source='pk', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
#    favorite_tusas = serializers.HyperlinkedRelatedField(
#        many=True,
#        read_only=False,
#        queryset=Tusa.objects.all(),
#       view_name='tusa-detail'
#    )

    class Meta:
        model = UserProfile
        depth = 1
        fields = ('url', 'id', 'username', 'email', 'first_name', 'last_name', 'description', 'user','user_url','avatar')

    def get_full_name(self, obj):
        request = self.context['request']
        return request.user.get_full_name()

    def update(self, instance, validated_data):
        # retrieve the User
        user_data = validated_data.pop('user', None)
        for attr, value in user_data.items():
            setattr(instance.user, attr, value)

        # retrieve Profile
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.user.save()
        instance.save()
        return instance

