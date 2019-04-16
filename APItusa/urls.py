from django.contrib import admin
from django.urls import path, include
from basic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('locations/', views.LocationsList.as_view()),
    path('locations/<int:pk>/',views.LocationDetail.as_view()),
    path('rest-auth/',include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('tusas/',views.TusasList.as_view()),
    path('tusas/<int:pk>',views.TusasDetail.as_view()),
]
