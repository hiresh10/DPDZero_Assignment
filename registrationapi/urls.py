from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *
router = DefaultRouter()
router.register(r'users', views.UserViewset, basename='user')

urlpatterns = [
    path("", views.SignupPage,name='signuppage'),
    path('register/',views.Register,name='register'),
    path('user_api/',include(router.urls)),
    path('auth/', include('rest_framework.urls',namespace='rest_framework_1')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
]
