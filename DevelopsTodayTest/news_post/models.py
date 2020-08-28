from django.db import models, IntegrityError
from django.utils import timezone


class NewsPost(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    creation_date = models.DateTimeField()
    upvote_amount = models.IntegerField()
    author_name = models.CharField(max_length=50)

    @staticmethod
    def create(title, link, author_name):
        instance = NewsPost(
            title=title,
            link=link,
            upvote_amount=0,
            author_name=author_name,
            creation_date=timezone.now(),
        )
        try:
            instance.save()
        except (ValueError, IntegrityError):
            return None

    @staticmethod
    def get_by_id(post_id):
        try:
            instance = NewsPost.objects.get(id=post_id)
            return instance
        except NewsPost.DoesNotExist:
            return None

    @staticmethod
    def filter(
        post_id=None,
        title=None,
        link=None,
        creation_date=None,
        upvote_amount=None,
        author_name=None,
    ):
        filter_data = {}
        if id is not None:
            filter_data["id"] = post_id
        if title is not None:
            filter_data["title"] = title
        if link is not None:
            filter_data["link"] = link
        if creation_date is not None:
            filter_data["creation_date"] = creation_date
        if upvote_amount is not None:
            filter_data["upvote_amount"] = upvote_amount
        if author_name is not None:
            filter_data["author_name"] = author_name

        result = NewsPost.objects.filter(**filter_data)
        return list(result)

    def __repr__(self):
        return (
            f"<NewsPost title:{self.title},"
            f" link:{self.link},"
            f" creation_date:{self.creation_date},"
            f" upvote_amount:{self.upvote_amount},"
            f"author_name:{self.author_name}>"
        )
