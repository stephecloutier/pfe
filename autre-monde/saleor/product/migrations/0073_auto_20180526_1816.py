# Generated by Django 2.0.3 on 2018-05-26 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0072_auto_20180526_1758'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productvariant',
            old_name='content_override',
            new_name='product_content_override',
        ),
    ]