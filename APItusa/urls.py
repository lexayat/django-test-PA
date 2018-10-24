from django.contrib import admin
from django.urls import path
from basic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addlocation/', views.add_location),
    path('gettusas/',views.get_list_of_tusas),
]
