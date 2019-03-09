from django import template
from app01 import models
from django.db.models import Count

register = template.Library()   # 生成一个注册的对象


@register.inclusion_tag('left_menu.html')
def get_left_menu(username):
    user = models.UserInfo.objects.filter(username=username).first()
    blog = user.blog
    category_list = models.Category.objects.filter(blog=blog).annotate(c=Count('article')).values('title', 'c')
    tag_list = models.Tag.objects.filter(blog=blog).annotate(c=Count('article')).values('title', 'c')
    # 按日期归档
    archive_list = models.Article.objects.filter(user=user).extra(
        select={'archive_ym': "date_format(create_time, '%%Y-%%m')"}
    ).values('archive_ym').annotate(c=Count('nid')).values('archive_ym', 'c')

    return {'category_list': category_list, 'tag_list': tag_list, 'archive_list': archive_list}