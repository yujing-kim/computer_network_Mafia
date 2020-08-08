# Generated by Django 3.0.6 on 2020-05-30 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=10)),
                ('c_job', models.CharField(max_length=10)),
                ('c_votes', models.IntegerField(default=0)),
                ('c_life', models.BooleanField(default=True)),
                ('c_img', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]