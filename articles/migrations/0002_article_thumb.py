# Generated by Django 2.1 on 2018-09-02 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default=True, upload_to=''),
        ),
    ]
