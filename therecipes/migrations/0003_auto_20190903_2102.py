# Generated by Django 2.2.3 on 2019-09-04 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('therecipes', '0002_auto_20190903_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='therecipes.Category'),
        ),
    ]
