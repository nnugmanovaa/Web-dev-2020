# Generated by Django 3.0.4 on 2020-04-02 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_remove_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_id',
            field=models.IntegerField(default=1),
        ),
    ]
