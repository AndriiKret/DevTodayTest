from django.db import models


class NewsPost(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    creation_date = models.DateTimeField()
    upvote_amount = models.IntegerField()
    author_name = models.CharField(max_length=50)

    @staticmethod
    def get_by_id(post_id):
        try:
            instance = NewsPost.objects.get(id=post_id)
            return instance
        except NewsPost.DoesNotExist:
            return None
