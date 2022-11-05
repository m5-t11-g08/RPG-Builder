from django.urls import path
from .views import UserView, LoginView, UserDetailView, UserUpdatePasswordView

urlpatterns = [
    path("", UserView.as_view()),
    path("login/", LoginView.as_view()),
    path("<pk>/", UserDetailView.as_view()),
    path("password/<pk>/", UserUpdatePasswordView.as_view())
]