# Generated by Django 4.1.2 on 2022-10-27 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0002_remove_clothes_category_subcategory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='gender',
            field=models.CharField(max_length=255, null=True),
        ),
    ]