# Generated by Django 4.2.1 on 2023-07-07 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0053_remove_tags_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='throttledapplication',
            name='post_logout_redirect_uris',
            field=models.TextField(blank=True, help_text='Allowed Post Logout URIs list, space separated'),
        ),
    ]
