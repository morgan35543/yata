# Generated by Django 2.0.7 on 2019-05-09 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0012_auto_20190509_0755'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='', max_length=16)),
                ('nItems', models.IntegerField(default=10)),
                ('lastScanTS', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Config',
        ),
    ]