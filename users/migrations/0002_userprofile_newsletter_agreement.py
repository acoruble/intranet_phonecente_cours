# Generated by Django 2.2.7 on 2019-11-25 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='newsletter_agreement',
            field=models.BooleanField(db_index=True, default=False, help_text='Une par semaine maximum', verbose_name='Recevoir des newsletter'),
        ),
    ]
