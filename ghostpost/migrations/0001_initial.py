# Generated by Django 2.2.13 on 2020-06-23 23:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoastOrRoast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boast_or_roast', models.BooleanField()),
                ('title', models.CharField(max_length=30)),
                ('post', models.CharField(max_length=280)),
                ('up_votes', models.IntegerField(default=0)),
                ('down_votes', models.IntegerField(default=0)),
                ('submit_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
