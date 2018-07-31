# Generated by Django 2.1a1 on 2018-06-08 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20180607_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='news_thumbnail',
        ),
        migrations.RemoveField(
            model_name='news',
            name='news_updated_date',
        ),
        migrations.AlterField(
            model_name='newsimg',
            name='img_news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News'),
        ),
    ]