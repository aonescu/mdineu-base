# Generated by Django 5.1.6 on 2025-02-25 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('image', models.URLField()),
                ('link_text', models.CharField(max_length=100)),
                ('link_icon', models.CharField(max_length=100)),
            ],
        ),
    ]
