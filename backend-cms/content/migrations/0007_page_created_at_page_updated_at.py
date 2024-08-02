# Generated by Django 5.0.7 on 2024-07-31 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_page_tab'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2024-01-01 00:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]