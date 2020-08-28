"""
    Comment serializer for API
"""
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Comment serializer class for API
    """

    class Meta:
        model = Comment
        fields = ['id', 'author_name', 'content', 'creation_date', 'post_id']
