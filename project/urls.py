from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import *
from tutorial.quickstart import views
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('student/', studentAPI.as_view()),
    path('student/<id>', studentAPI.as_view()),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
   
   
