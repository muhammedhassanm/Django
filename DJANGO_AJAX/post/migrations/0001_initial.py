# Generated by Django 2.2.4 on 2020-08-31 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_heading', models.CharField(max_length=200)),
                ('post_text', models.TextField()),
                ('post_author', models.CharField(default='anonymous', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete='CASCADE', to='post.Post')),
            ],
        ),
    ]
