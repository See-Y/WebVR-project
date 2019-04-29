# Generated by Django 2.1.7 on 2019-04-29 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebVR', '0002_auto_20190308_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='a_circle',
            name='height',
        ),
        migrations.RemoveField(
            model_name='a_circle',
            name='width',
        ),
        migrations.RemoveField(
            model_name='a_cone',
            name='width',
        ),
        migrations.RemoveField(
            model_name='a_cylinder',
            name='width',
        ),
        migrations.RemoveField(
            model_name='a_icosahedron',
            name='height',
        ),
        migrations.RemoveField(
            model_name='a_icosahedron',
            name='width',
        ),
        migrations.RemoveField(
            model_name='a_sphere',
            name='height',
        ),
        migrations.RemoveField(
            model_name='a_sphere',
            name='width',
        ),
        migrations.AlterField(
            model_name='a_cone',
            name='height',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
        ),
    ]