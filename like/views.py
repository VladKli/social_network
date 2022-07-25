from datetime import date
from datetime import timedelta

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Like
from .serializers import LikeSerializer
from rest_framework import permissions, status


class LikeView(APIView):
    """Like/dislike a post"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.data['user'] = self.request.user.id
        request.data['post'] = self.kwargs.get("pk")
        serializer = LikeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        like = Like.objects.get(user=self.request.user.id, post=self.kwargs.get("pk"))
        like.delete()
        return Response("You unliked a post.", status=status.HTTP_200_OK)


class LikeAnalyticsView(APIView):
    """Get analytics with optional date parameters"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        queryset = Like.objects.all()
        date_from = self.request.query_params.get("date_from")
        date_to = self.request.query_params.get("date_to")

        if date_from is not None:
            queryset = queryset.filter(date__gte=date_from)
        if date_to is not None:
            queryset = queryset.filter(
                date__lte=date.fromisoformat(date_to) + timedelta(days=1)
            )

        serializer = LikeSerializer(queryset, many=True)
        return Response(serializer.data)
