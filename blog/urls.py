from django.urls import include, path, re_path
from . import views, feed

urlpatterns = [
    path('feed/', feed.LatestPosts(), name='feed'),
    path('', views.BlogIndex.as_view(), name='index'),
    re_path(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
]
