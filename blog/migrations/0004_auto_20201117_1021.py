# Generated by Django 2.2.3 on 2020-11-17 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201117_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
