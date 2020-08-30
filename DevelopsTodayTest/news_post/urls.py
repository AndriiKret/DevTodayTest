from django.urls import path
from news_post.views import (
    news_post_list_view,
    news_post_detailed_view,
    news_post_upvote,
)

urlpatterns = [
    path("", news_post_list_view, name="all_posts"),
    path("<pk>", news_post_detailed_view, name="detailed_post"),
    path("<pk>/upvote/", news_post_upvote, name="post_upvote"),
]
