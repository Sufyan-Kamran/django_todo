# Generated by Django 3.2.9 on 2022-10-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_auto_20221004_0050'),
    ]

    operations = [
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('nid', models.IntegerField()),
                ('username', models.CharField(max_length=50)),
                ('notice_title', models.CharField(max_length=100)),
                ('notice', models.CharField(max_length=1000)),
                ('notice_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('completion_date', models.DateField()),
            ],
        ),
    ]
