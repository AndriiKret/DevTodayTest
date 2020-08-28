from rest_framework import viewsets, status
from rest_framework.decorators import action
from .models import NewsPost
from .serializers import NewsPostSerializer

from rest_framework.response import Response


class NewsPostViewSet(viewsets.ModelViewSet):
    """
    NewsPost view set
    """
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk):
        instance = NewsPost.get_by_id(pk)
        instance.upvote_amount += 1
        instance.save()
        return Response(status=status.HTTP_200_OK)


news_post_list_view = NewsPostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
news_post_detailed_view = NewsPostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
news_post_upvote = NewsPostViewSet.as_view({
    'post': 'upvote'
})
