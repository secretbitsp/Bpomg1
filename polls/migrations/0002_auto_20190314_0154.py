# Generated by Django 2.1.5 on 2019-03-14 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='gepkocsirendszama',
            field=models.CharField(help_text='Példa: AAA - 111', max_length=7),
        ),
    ]