# Generated by Django 3.2.5 on 2021-07-19 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publics', '0002_auto_20210719_0604'),
        ('admins', '0002_auto_20210719_0603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='number',
        ),
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='admin',
            name='public',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publics', to='publics.public'),
        ),
    ]
