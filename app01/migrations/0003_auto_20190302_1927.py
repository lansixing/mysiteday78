# Generated by Django 2.1.7 on 2019-03-02 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20190302_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comment_count',
            field=models.IntegerField(default=0, verbose_name='点赞数'),
        ),
        migrations.AddField(
            model_name='article',
            name='down_count',
            field=models.IntegerField(default=0, verbose_name='踩数'),
        ),
        migrations.AddField(
            model_name='article',
            name='up_count',
            field=models.IntegerField(default=0, verbose_name='点赞数'),
        ),
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.CharField(max_length=255, verbose_name='文章描述'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, verbose_name='文章标题'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=True, to='app01.Comment'),
        ),
    ]
