# Generated by Django 4.1 on 2022-08-25 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elapp', '0002_elmodel_duedate_elmodel_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=25)),
                ('date', models.DateField()),
            ],
        ),
    ]