# Generated by Django 4.1.5 on 2023-01-13 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=34)),
                ('password', models.TextField()),
                ('phone', models.CharField(max_length=30)),
            ],
        ),
    ]
