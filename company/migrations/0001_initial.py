# Generated by Django 3.1.2 on 2020-11-17 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tId', models.IntegerField(default=0, unique=True)),
                ('name', models.CharField(default='Default company name', max_length=32)),
                ('cost', models.BigIntegerField(default=0)),
                ('default_employees', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Default position name', max_length=32)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.companydescription')),
            ],
        ),
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Default position name', max_length=32)),
                ('effect', models.CharField(default='Default position name', max_length=128)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.companydescription')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Default position name', max_length=32)),
                ('description', models.CharField(default='Default description', max_length=128)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.companydescription')),
            ],
        ),
    ]