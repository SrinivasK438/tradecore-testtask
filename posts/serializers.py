from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'author',
            'title',
            'content',
            'posted_on',
        )
        extra_kwargs = {
            'author': {
                'read_only': True,
            },
            'posted_on': {
                'read_only': True,
            }
        }
