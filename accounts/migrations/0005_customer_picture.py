# Generated by Django 3.0.8 on 2020-07-16 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
