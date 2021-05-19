from rest_framework import serializers

from posts.models import Post
from users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'author',
            'title',
            'content',
            'posted_on',
        )
        extra_kwargs = {
            'posted_on': {
                'read_only': True,
            }
        }