# Generated by Django 5.0.4 on 2024-05-26 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0005_alter_coursearticle_article_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название задания')),
                ('text', models.TextField(verbose_name='Текст задания')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='articles.article', verbose_name='Статья занятия')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
                'ordering': ['name'],
            },
        ),
    ]