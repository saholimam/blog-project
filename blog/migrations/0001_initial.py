# Generated by Django 3.1.4 on 2020-12-03 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('time', models.DateTimeField(auto_now=True)),
                ('blog', models.CharField(max_length=1024)),
            ],
        ),
    ]
