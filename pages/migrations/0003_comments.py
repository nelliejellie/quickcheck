# Generated by Django 3.2.5 on 2021-07-21 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210720_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('by', models.CharField(max_length=14)),
                ('comment_id', models.IntegerField()),
                ('parent', models.IntegerField()),
                ('Text', models.TextField()),
                ('time', models.IntegerField()),
                ('type', models.CharField(max_length=20)),
            ],
        ),
    ]