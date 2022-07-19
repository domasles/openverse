# Generated by Django 4.0.6 on 2022-07-15 11:48

from django.db import migrations
import oauth2_provider.generators
import oauth2_provider.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0047_help_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='throttledapplication',
            name='client_secret',
            field=oauth2_provider.models.ClientSecretField(blank=True, db_index=True, default=oauth2_provider.generators.generate_client_secret, help_text='Hashed on Save. Copy it now if this is a new secret.', max_length=255),
        ),
    ]
