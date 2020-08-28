# Generated by Django 3.1 on 2020-08-28 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('news_post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=255)),
                ('creation_date', models.DateTimeField()),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_post.newspost')),
            ],
        ),
    ]
