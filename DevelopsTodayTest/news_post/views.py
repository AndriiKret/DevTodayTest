from rest_framework import viewsets
from .models import NewsPost
from .serializers import NewsPostSerializer


class NewsPostViewSet(viewsets.ModelViewSet):
    """
    NewsPost view set
    """
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer


news_post_list_view = NewsPostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
news_post_detailed_view = NewsPostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
