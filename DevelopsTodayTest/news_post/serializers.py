"""
    NewsPost serializer for API
"""
from rest_framework import serializers
from news_post.models import NewsPost


class NewsPostSerializer(serializers.ModelSerializer):
    """
    NewsPost serializer class for API
    """

    class Meta:
        model = NewsPost
        fields = [
            "id",
            "title",
            "link",
            "creation_date",
            "upvote_amount",
            "author_name",
        ]
