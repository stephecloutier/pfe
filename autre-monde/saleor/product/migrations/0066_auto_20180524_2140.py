# Generated by Django 2.0.3 on 2018-05-24 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0065_auto_20180524_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='product_reference',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
