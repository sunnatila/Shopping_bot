# Generated by Django 4.2.4 on 2023-08-23 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_category_id_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mention',
            field=models.CharField(default=10, max_length=50),
            preserve_default=False,
        ),
    ]