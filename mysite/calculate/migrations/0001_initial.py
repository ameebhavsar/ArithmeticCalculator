# Generated by Django 5.0 on 2024-01-01 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_a', models.IntegerField()),
                ('input_b', models.IntegerField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
