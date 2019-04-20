from django.contrib import admin
from django.urls import path, include
from basic.views import TusasList,TusasDetail
from userProfile.views import UserListAPIView
from userProfile.views import UserListDetail
from userProfile.views import UserViewSet
from userProfile.views import ProfileViewSet
from userProfile.views import TusasViewSet

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'tusas', TusasViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/',include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    #path('tusas/',TusasList.as_view()),
    #path('tusas/<int:pk>',TusasDetail.as_view()),
    path('', include(router.urls)),
    #path('users/',UserListAPIView.as_view()),
    #path('users/<int:pk>/',UserListDetail.as_view()),
    #path('users/', UserViewSet.as_view()),
    #path('profiles/', ProfileViewSet.as_view()),
]
