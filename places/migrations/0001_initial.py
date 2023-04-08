# Generated by Django 3.2 on 2023-04-08 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description_short', models.TextField()),
                ('description_long', models.TextField()),
                ('lng', models.CharField(max_length=50)),
                ('lat', models.CharField(max_length=50)),
            ],
        ),
    ]
