# Generated by Django 5.0.6 on 2024-05-25 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0003_delete_asset_textpdf_descr_alter_textpdf_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textpdf',
            name='descr',
            field=models.TextField(max_length=200),
        ),
    ]
