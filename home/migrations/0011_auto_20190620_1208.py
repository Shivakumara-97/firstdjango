# Generated by Django 2.2.2 on 2019-06-20 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20190619_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='total_book_written',
            field=models.CharField(blank=True, choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')], help_text='total_book_written', max_length=1),
        ),
    ]
