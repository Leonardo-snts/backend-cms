# Generated by Django 5.0.7 on 2024-07-22 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='template',
            field=models.CharField(choices=[('template1', 'Template 1'), ('template2', 'Template 2')], default='template1', max_length=50),
        ),
    ]
