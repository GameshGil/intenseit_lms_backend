# Generated by Django 5.0.4 on 2024-05-26 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_coursearticle_article_and_more'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='lesson',
        ),
        migrations.AddField(
            model_name='task',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='articles.article', verbose_name='Статья задания'),
        ),
    ]
