# Generated by Django 5.0.4 on 2024-05-07 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_options_article_area_and_more'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursearticle',
            options={'ordering': ['course', 'order_num']},
        ),
        migrations.AlterField(
            model_name='article',
            name='courses',
            field=models.ManyToManyField(related_name='lessons', through='articles.CourseArticle', to='courses.course'),
        ),
    ]
