# Generated by Django 4.2.4 on 2023-09-15 16:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('content', models.TextField()),
                ('excerpt', models.TextField()),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(default='draft', max_length=10)),
                ('author', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'blogs',
            },
        ),
    ]