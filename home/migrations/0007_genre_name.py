# Generated by Django 2.2.2 on 2019-06-19 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_genre_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Book Name', max_length=100, null=True),
        ),
    ]
