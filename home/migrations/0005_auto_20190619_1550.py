# Generated by Django 2.2.2 on 2019-06-19 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190619_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='total_book_written',
            field=models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')], max_length=1),
        ),
    ]
