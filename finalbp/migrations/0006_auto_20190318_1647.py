# Generated by Django 2.1.5 on 2019-03-18 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalbp', '0005_auto_20190318_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hahudeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(max_length=100)),
                ('marka', models.CharField(max_length=100)),
                ('kategoria', models.CharField(max_length=100)),
                ('modell', models.CharField(max_length=100)),
                ('tipus', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='hahuautok',
            name='kategoria',
        ),
        migrations.RemoveField(
            model_name='hahuautok',
            name='marka',
        ),
        migrations.RemoveField(
            model_name='hahuautok',
            name='modell',
        ),
        migrations.RemoveField(
            model_name='hahuautok',
            name='rank',
        ),
        migrations.RemoveField(
            model_name='hahuautok',
            name='tipus',
        ),
    ]