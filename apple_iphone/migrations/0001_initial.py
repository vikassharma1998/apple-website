# Generated by Django 4.0.3 on 2022-04-21 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IphoneModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_information', models.TextField()),
                ('image', models.ImageField(upload_to='pics')),
                ('summary_name', models.CharField(max_length=100)),
                ('summary_description', models.TextField()),
                ('network', models.CharField(default='Network', max_length=100)),
                ('network_description', models.TextField()),
                ('display', models.CharField(default='Display', max_length=100)),
                ('display_description', models.TextField()),
                ('memory', models.CharField(default='Memory', max_length=100)),
                ('memory_description', models.TextField()),
                ('camera', models.CharField(default='Camera', max_length=100)),
                ('camera_description', models.TextField()),
                ('battery', models.CharField(default='Battery', max_length=100)),
                ('battery_description', models.TextField()),
            ],
        ),
    ]
