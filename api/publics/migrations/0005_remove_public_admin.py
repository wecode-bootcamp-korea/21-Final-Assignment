# Generated by Django 3.2.5 on 2021-07-21 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publics', '0004_rename_paymeny_public_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='public',
            name='admin',
        ),
    ]