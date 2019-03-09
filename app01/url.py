from django.conf.urls import url
from app01 import views

urlpatterns = [
    url(r'backend/add_article/', views.add_article),
    url(r'up_down/', views.up_down),
    url(r'comment/', views.comment),
    url(r'comment_tree/(\d+)', views.comment_tree),
    url(r'(?P<username>\w+)/article/(?P<pk>\d+)/$', views.article_detail),  # 文章详情
    url(r'(?P<username>\w+)/$', views.home),  # home(request, username)

]
