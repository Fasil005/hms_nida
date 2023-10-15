# Generated by Django 3.0.5 on 2023-10-11 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='biometric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField(max_length=10)),
                ('weight', models.IntegerField(max_length=10)),
                ('bloodpressure', models.CharField(max_length=100)),
                ('bloodgroup', models.CharField(max_length=15)),
            ],
        ),
    ]
