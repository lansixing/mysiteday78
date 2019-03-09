"""mysiteday76 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url, include
from app01 import url as blog_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload),
    path('register/', views.register),
    path('index/', views.index),
    # 将所有已blog开头的url都交给mysiteday68下面的url.py来处理
    path('blog/', include(blog_url)),
    path('login/', views.login),
    # path('get_valid_img.png/', views.get_valid_img),
    # 极验滑动验证码，获取验证码的url
    path('pc-geetest/register', views.get_geetest),
    # 专门用来校验用户名是否已经被注册的借口
    path('logout/', views.logout),
    # media相关的路由设置
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    path('upload_kind/', views.upload_kind)
]
