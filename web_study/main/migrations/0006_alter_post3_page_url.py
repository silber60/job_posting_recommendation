# Generated by Django 4.0.6 on 2022-08-05 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_post3_delete_post2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post3',
            name='page_url',
            field=models.CharField(max_length=2000),
        ),
    ]
