# Generated by Django 2.1.7 on 2019-04-20 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_creation', '0002_auto_20190420_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket_details',
            name='file',
            field=models.CharField(default=None, max_length=256, null=True),
        ),
    ]
