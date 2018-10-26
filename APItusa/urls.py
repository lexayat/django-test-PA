from django.contrib import admin
from django.urls import path
from basic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('locations/', views.LocationsList.as_view()),
    path('locations/<int:pk>/',views.LocationDetail.as_view()),
]
