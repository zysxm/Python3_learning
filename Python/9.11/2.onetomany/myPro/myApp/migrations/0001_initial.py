# Generated by Django 2.1.1 on 2018-09-11 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
                ('source', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Card',
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('car_num', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'people',
            },
        ),
        migrations.AddField(
            model_name='card',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.People'),
        ),
    ]
