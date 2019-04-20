from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics,viewsets, mixins, permissions
from userProfile.models import UserProfile
from userProfile.serializers import UserProfileSerializer
from userProfile.serializers import UserSerializer
from basic.models import Tusa
from basic.serializers import TusaSerializer
from rest_framework.views import APIView
from userProfile.permissions import (
    IsOwnerOrReadOnly, IsAdminUserOrReadOnly, IsSameUserAllowEditionOrReadOnly
)


# Create your views here.

class UserListAPIView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsSameUserAllowEditionOrReadOnly,)


class ProfileViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

class TusasViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Tusa.objects.all()
    serializer_class = TusaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminUserOrReadOnly)




