from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ["id", "author", "title", "content", "likes_count", "post_date"]

    def _user(self, obj):
        request = self.context.get('request', None)
        if request:
            return request.user
