# Generated by Django 4.1.3 on 2022-12-04 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises_app', '0008_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='end_publish_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='start_publish_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.IntegerField(choices=[(0, 'in progress'), (1, 'waiting'), (2, 'published')], default=0),
        ),
    ]
