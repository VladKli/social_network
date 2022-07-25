from django.urls import path
from .views import RegisterApi, ActivityApi

urlpatterns = [
      path('register/', RegisterApi.as_view()),
      path('activity/', ActivityApi.as_view()),

]
