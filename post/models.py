from django.db import models


class Post(models.Model):
    """Post class"""

    author = models.ForeignKey('auth.User', related_name='owner', on_delete=models.PROTECT)
    title = models.CharField(max_length=300, unique=True)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    def likes_count(self):
        return self.likes.all().count()

    def __str__(self):
        return self.title
