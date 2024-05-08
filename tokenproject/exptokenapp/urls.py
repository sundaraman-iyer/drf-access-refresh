from django.urls import path
from .views import RegisterAPIView, LoginAPIView, UserAPIView
urlpatterns = [
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('users', UserAPIView.as_view())

]