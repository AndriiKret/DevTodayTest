from django.urls import path
from .views import news_post_list_view, news_post_detailed_view

urlpatterns = [
    path('', news_post_list_view, name='all_posts'),
    path('<pk>', news_post_detailed_view, name='detailed_post'),
]
