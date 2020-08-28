from django.urls import path
from .views import comment_detailed_view, comment_list_view

urlpatterns = [
    path('', comment_list_view, name='all_comments'),
    path('<pk>', comment_detailed_view, name='detailed_comment'),
]
