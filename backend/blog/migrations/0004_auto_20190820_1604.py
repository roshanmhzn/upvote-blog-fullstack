# Generated by Django 2.2.4 on 2019-08-20 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_date',
            new_name='created',
        ),
    ]