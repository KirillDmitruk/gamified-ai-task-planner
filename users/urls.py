from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserListAPIView, UserRetrieveAPIView,UserUpdateAPIView, UserDestroyAPIView, UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
path('register/', UserCreateAPIView.as_view(), name='users_create'),
path('', UserListAPIView.as_view(), name='users_list'),
path('detail/<int:pk>/', UserRetrieveAPIView.as_view(), name='users_detail'),
path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='users_update'),
path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='users_delete'),
# token
path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token_obtain_pair'),
# Доступ к токену неавт. пользоват.
path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
