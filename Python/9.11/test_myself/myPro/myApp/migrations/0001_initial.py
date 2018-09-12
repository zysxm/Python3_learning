# Generated by Django 2.1.1 on 2018-09-11 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('card_code', models.OneToOneField(on_delete=True, primary_key=True, serialize=False, to='myApp.People')),
                ('card_type', models.CharField(max_length=20)),
            ],
        ),
    ]
