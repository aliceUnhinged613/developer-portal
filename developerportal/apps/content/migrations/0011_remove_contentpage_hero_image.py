# Generated by Django 2.2.12 on 2020-05-07 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_copy_hero_image_field_to_card_image_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentpage',
            name='hero_image',
        ),
    ]