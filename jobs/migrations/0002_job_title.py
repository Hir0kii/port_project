# Generated by Django 3.0.3 on 2020-05-13 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
    ]