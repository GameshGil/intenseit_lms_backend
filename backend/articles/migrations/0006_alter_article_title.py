# Generated by Django 5.0.4 on 2024-07-06 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_coursearticle_article_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Заголовок статьи'),
        ),
    ]
