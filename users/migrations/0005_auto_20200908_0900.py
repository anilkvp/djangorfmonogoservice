# Generated by Django 2.2.12 on 2020-09-08 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200908_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]