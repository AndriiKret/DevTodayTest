from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from comment.models import Comment
from comment.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    Comment view set
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["post_id"]


comment_list_view = CommentViewSet.as_view({"get": "list", "post": "create"})
comment_detailed_view = CommentViewSet.as_view(
    {"get": "retrieve", "put": "update", "delete": "destroy"}
)
