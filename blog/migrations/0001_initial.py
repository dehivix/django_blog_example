# Generated by Django 2.1 on 2018-09-18 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('publish', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Blog Entries',
                'verbose_name': 'Blog Entry',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
