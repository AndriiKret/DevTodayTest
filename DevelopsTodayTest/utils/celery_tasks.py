from celery.task import periodic_task
from celery.schedules import crontab

from news_post.models import NewsPost


@periodic_task(run_every=(crontab(hour=1, minute=30)), name="task-clean")
def clean_upvote():
    posts = NewsPost.objects.all()
    for post in posts:
        post.upvote_amount = 0
        post.save()
