from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CommentViewSet(viewsets.ModelViewSet):
    """
    Comment view set
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post_id']

    # def get_queryset(self):
    #     queryset = Comment.objects.all()



comment_list_view = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
comment_detailed_view = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
