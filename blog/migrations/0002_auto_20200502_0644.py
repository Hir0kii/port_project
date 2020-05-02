# Generated by Django 3.0.5 on 2020-05-02 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='text',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='published_date',
            new_name='pub_date',
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
