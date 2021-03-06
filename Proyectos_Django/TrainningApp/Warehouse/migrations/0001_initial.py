# Generated by Django 3.1.4 on 2020-12-17 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('description', models.TextField(default='Description here', max_length=20)),
                ('create_date', models.DateTimeField(verbose_name='Date creation')),
                ('update_date', models.DateTimeField(verbose_name='Date update')),
            ],
        ),
        migrations.CreateModel(
            name='Provide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField(max_length=20)),
                ('address', models.TextField(max_length=60)),
                ('status', models.BooleanField(default=True)),
                ('description', models.TextField(default='Description here', max_length=20)),
                ('create_date', models.DateTimeField(verbose_name='Date creation')),
                ('update_date', models.DateTimeField(verbose_name='Date update')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('description', models.TextField(default='Description here', max_length=20)),
                ('create_date', models.DateTimeField(verbose_name='Date creation')),
                ('update_date', models.DateTimeField(verbose_name='Date update')),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Warehouse.category')),
            ],
        ),
    ]
