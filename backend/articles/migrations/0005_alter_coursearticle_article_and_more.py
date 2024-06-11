# Generated by Django 5.0.4 on 2024-05-26 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_coursearticle_order_num'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursearticle',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article', verbose_name='Статья занятия'),
        ),
        migrations.AlterField(
            model_name='coursearticle',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Курс занятия'),
        ),
    ]