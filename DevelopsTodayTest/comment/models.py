from django.db import models
from news_post.models import NewsPost


class Comment(models.Model):
    author_name = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    creation_date = models.DateTimeField()
    post_id = models.ForeignKey(NewsPost, on_delete=models.CASCADE, null=False)
