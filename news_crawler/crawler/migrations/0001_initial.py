# Generated by Django 2.0.7 on 2019-02-13 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=25)),
                ('datePublished', models.DateTimeField()),
                ('image', models.URLField()),
                ('context', models.TextField()),
            ],
            options={
                'db_table': 'news',
            },
        ),
    ]
