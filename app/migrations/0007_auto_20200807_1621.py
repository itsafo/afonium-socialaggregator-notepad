# Generated by Django 2.1.15 on 2020-08-07 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200807_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default='Choose Category', on_delete=django.db.models.deletion.CASCADE, to='app.Category', verbose_name='Category'),
        ),
    ]