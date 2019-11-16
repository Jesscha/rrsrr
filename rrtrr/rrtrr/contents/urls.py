from django.urls import path, re_path

from rrtrr.contents.views import (
    ContentsHomeView,
    ContentsListView,
    ContentCreateView,
    ContentsDetailView
)

app_name = "contents"
urlpatterns = [
    re_path(r'^$', ContentsHomeView.as_view()),
    re_path(r'^list/$', ContentsListView.as_view()),
    re_path(r'^create/$', ContentCreateView.as_view()),
    re_path(r'^detail/(?P<id>\d+)/$', ContentsDetailView.as_view(),),
]
