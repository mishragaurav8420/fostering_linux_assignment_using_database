# Generated by Django 4.1.7 on 2023-05-29 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_alter_book_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
