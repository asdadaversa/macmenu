# Generated by Django 5.0.4 on 2024-04-09 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latinos_name', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField(null=True)),
                ('calories', models.CharField(max_length=63)),
                ('fats', models.CharField(max_length=63)),
                ('carbs', models.CharField(max_length=63)),
                ('proteins', models.CharField(max_length=63)),
                ('unsaturated_fats', models.CharField(max_length=63)),
                ('sugar', models.CharField(max_length=63)),
                ('salt', models.CharField(max_length=63)),
                ('portion', models.CharField(max_length=63)),
            ],
        ),
    ]