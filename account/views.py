from rest_framework import generics
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer, UserActivitySerializer
from django.contrib.auth.models import User


class RegisterApi(generics.GenericAPIView):
    """Register user"""
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "message": "User Created Successfully.  Now perform Login to get your token",
            }
        )


class ActivityApi(generics.GenericAPIView):
    """Check last login, activity"""

    serializer_class = UserActivitySerializer

    def get(self, request):
        queryset = User.objects.all()
        serializer = UserActivitySerializer(queryset, many=True)
        return Response(serializer.data)
