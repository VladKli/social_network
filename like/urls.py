from django.urls import path
from .views import LikeView, LikeAnalyticsView

urlpatterns = [
      path("<int:pk>/", LikeView.as_view()),
      path("analytics/", LikeAnalyticsView.as_view()),
]
