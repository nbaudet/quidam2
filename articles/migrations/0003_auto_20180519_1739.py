# Generated by Django 2.0.5 on 2018-05-19 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20180519_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='picture',
            field=models.ImageField(null=True, upload_to='category_<django.db.models.fields.CharField>'),
        ),
        migrations.AddField(
            model_name='categorydescription',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
