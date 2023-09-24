# Generated by Django 4.2.5 on 2023-09-22 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]