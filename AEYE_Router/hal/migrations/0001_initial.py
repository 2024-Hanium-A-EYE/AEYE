# Generated by Django 3.2 on 2024-08-06 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aeye_inference_models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whoami', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
