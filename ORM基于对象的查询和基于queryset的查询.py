from app01 import models
from django.db.models import Count
user = models.UserInfo.objects.filter(username='yimi').first()
blog = user.blog
ret = models.Category.objects.filter(blog=blog)
ret = ret[0].article_set.all()
ret.annotate(a=Count('article'))
for i in ret:
    print(i.title, i.article_set.all().count())
