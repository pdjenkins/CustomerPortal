# Generated by Django 3.1.3 on 2020-11-19 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custport', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='CC_info',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]
