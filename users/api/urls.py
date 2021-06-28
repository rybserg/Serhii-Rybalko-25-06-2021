from django.urls import path
from users.api.views import UserEmailListAPIView, CurrentUserAPIView, UserListAPIView


urlpatterns = [
    path("user/", CurrentUserAPIView.as_view(), name="current-user"),
    path("users/", UserListAPIView.as_view(), name="users"),
    path("users/<int:pk>/emails/", UserEmailListAPIView.as_view(), name="user-emails"),
]