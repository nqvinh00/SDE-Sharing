# Generated by Django 2.2.4 on 2020-03-26 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slide_id', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=100)),
                ('teacher', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=200)),
            ],
        ),
    ]
