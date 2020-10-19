# Generated by Django 3.1.2 on 2020-10-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogram', '0002_auto_20201019_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='photo',
            name='comments',
        ),
        migrations.AddField(
            model_name='profile',
            name='comments',
            field=models.ManyToManyField(to='photogram.comments'),
        ),
        migrations.AddField(
            model_name='photo',
            name='comments',
            field=models.ManyToManyField(to='photogram.comments'),
        ),
    ]