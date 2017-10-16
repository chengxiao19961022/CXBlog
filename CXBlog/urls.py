from django.conf.urls import url
# from . import views,view_tabletest
# from . import search_test
from . import views
from .feeds import LatestPostsFeed

urlpatterns = [
    # post views
    url(r'^blog_test/$', views.post_list, name='post_list'),
    # url(r'^$', views.PostListView.as_view(),name='post_list'),
    # url(r'^upload', views.simple_list, name='upload_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    # url(r'^search-post$', search_test.search_post),
    # url(r'^confirm-task$', views.confirm_task),
    # url(r'^task-list$', views.added_task),
    # url(r'^task-detail$', views.task_detail),
    # url(r'^index$', views.index),
    # url(r'^tabletest', view_tabletest.table1),
    # url(r'^login', views.login),
    url(r'^(?P<post_id>\d+)/share/$', views.post_share,
        name='post_share'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$',views.blog_test,
        name='post_list_by_tag'),
    url(r'^feed/$', LatestPostsFeed(), name='post_feed'),
    url(r'^test/$', views.test, name='test'),
    url(r'^$', views.blog_test, name='blog_test'),
]
