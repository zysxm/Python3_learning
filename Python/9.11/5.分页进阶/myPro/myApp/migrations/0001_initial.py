# Generated by Django 2.1.1 on 2018-09-12 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('des', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'goods',
            },
        ),
    ]
