# Generated by Django 4.1.2 on 2023-03-02 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_song_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='song',
            name='cover_image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_title',
            field=models.CharField(max_length=200),
        ),
    ]
