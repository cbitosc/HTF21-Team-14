# Generated by Django 3.0.8 on 2021-10-29 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='state',
            field=models.CharField(choices=[('ACCEPT', 'ACCEPT'), ('REJECT', 'reject'), ('REQUESTED', 'requested')], default='REQUESTED', max_length=20),
        ),
    ]
