# Generated by Django 3.1.5 on 2021-05-21 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0019_auto_20210102_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiCallLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField(default=0)),
                ('url', models.CharField(blank=True, default='', max_length=256)),
                ('error', models.IntegerField(default=-1)),
            ],
        ),
    ]