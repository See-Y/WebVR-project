# Generated by Django 2.1.7 on 2019-03-02 16:10

import colorful.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='empty', max_length=200)),
                ('changed_date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='animation',
            fields=[
                ('basic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='WebVR.Basic')),
            ],
            bases=('WebVR.basic',),
        ),
        migrations.CreateModel(
            name='position',
            fields=[
                ('pos_basic', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='WebVR.Basic')),
                ('pos_x', models.FloatField(default=0)),
                ('pos_y', models.FloatField(default=0)),
                ('pos_z', models.FloatField(default=0)),
            ],
            bases=('WebVR.basic',),
        ),
        migrations.CreateModel(
            name='rotation',
            fields=[
                ('rot_basic', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='WebVR.Basic')),
                ('rot_x', models.FloatField(default=0)),
                ('rot_y', models.FloatField(default=0)),
                ('rot_z', models.FloatField(default=0)),
            ],
            bases=('WebVR.basic',),
        ),
        migrations.CreateModel(
            name='scale',
            fields=[
                ('sca_basic', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='WebVR.Basic')),
                ('sca_x', models.FloatField(default=1)),
                ('sca_y', models.FloatField(default=1)),
                ('sca_z', models.FloatField(default=1)),
            ],
            bases=('WebVR.basic',),
        ),
        migrations.CreateModel(
            name='shadow',
            fields=[
                ('sha_basic', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='WebVR.Basic')),
                ('cast', models.BooleanField(default=False)),
                ('receive', models.BooleanField(default=False)),
            ],
            bases=('WebVR.basic',),
        ),
        migrations.CreateModel(
            name='a_box',
            fields=[
                ('scale_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.scale')),
                ('position_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.position')),
                ('rotation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.rotation')),
                ('shadow_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='WebVR.shadow')),
                ('name', models.CharField(max_length=50)),
                ('color', colorful.fields.RGBColorField(default=['#FF0000', '#00FF00', '#0000FF'])),
                ('src', models.TextField(default='')),
                ('visible', models.BooleanField(default=False)),
                ('depth', models.FloatField(default=1)),
                ('height', models.FloatField(default=1)),
                ('width', models.FloatField(default=1)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebVR.Project')),
            ],
            options={
                'abstract': False,
            },
            bases=('WebVR.shadow', 'WebVR.rotation', 'WebVR.position', 'WebVR.scale'),
        ),
        migrations.CreateModel(
            name='a_circle',
            fields=[
                ('scale_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.scale')),
                ('position_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.position')),
                ('rotation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.rotation')),
                ('shadow_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='WebVR.shadow')),
                ('name', models.CharField(max_length=50)),
                ('color', colorful.fields.RGBColorField(default=['#FF0000', '#00FF00', '#0000FF'])),
                ('src', models.TextField(default='')),
                ('visible', models.BooleanField(default=False)),
                ('radius', models.FloatField(default=1)),
                ('height', models.FloatField(default=256)),
                ('width', models.FloatField(default=512)),
                ('theta_length', models.FloatField(default=360)),
                ('theta_start', models.FloatField(default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebVR.Project')),
            ],
            options={
                'abstract': False,
            },
            bases=('WebVR.shadow', 'WebVR.rotation', 'WebVR.position', 'WebVR.scale'),
        ),
        migrations.CreateModel(
            name='a_cone',
            fields=[
                ('scale_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.scale')),
                ('position_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.position')),
                ('rotation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.rotation')),
                ('shadow_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='WebVR.shadow')),
                ('name', models.CharField(max_length=50)),
                ('color', colorful.fields.RGBColorField(default=['#FF0000', '#00FF00', '#0000FF'])),
                ('src', models.TextField(default='')),
                ('visible', models.BooleanField(default=False)),
                ('radius_bottom', models.FloatField(default=1)),
                ('radius_top', models.FloatField(default=0.8)),
                ('theta_length', models.FloatField(default=360)),
                ('theta_start', models.FloatField(default=0)),
                ('width', models.FloatField(default=512)),
                ('height', models.FloatField(default=256)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebVR.Project')),
            ],
            options={
                'abstract': False,
            },
            bases=('WebVR.shadow', 'WebVR.rotation', 'WebVR.position', 'WebVR.scale'),
        ),
        migrations.CreateModel(
            name='a_cylinder',
            fields=[
                ('scale_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.scale')),
                ('position_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.position')),
                ('rotation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.rotation')),
                ('shadow_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='WebVR.shadow')),
                ('name', models.CharField(max_length=50)),
                ('color', colorful.fields.RGBColorField(default=['#FF0000', '#00FF00', '#0000FF'])),
                ('src', models.TextField(default='')),
                ('visible', models.BooleanField(default=False)),
                ('radius_bottom', models.FloatField(default=1)),
                ('radius_top', models.FloatField(default=0.8)),
                ('theta_length', models.FloatField(default=360)),
                ('theta_start', models.FloatField(default=0)),
                ('width', models.FloatField(default=512)),
                ('height', models.FloatField(default=256)),
                ('open_ended', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebVR.Project')),
            ],
            options={
                'abstract': False,
            },
            bases=('WebVR.shadow', 'WebVR.rotation', 'WebVR.position', 'WebVR.scale'),
        ),
        migrations.CreateModel(
            name='a_dodecahedron',
            fields=[
                ('scale_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.scale')),
                ('position_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.position')),
                ('rotation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.rotation')),
                ('shadow_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='WebVR.shadow')),
                ('name', models.CharField(max_length=50)),
                ('color', colorful.fields.RGBColorField(default=['#FF0000', '#00FF00', '#0000FF'])),
                ('src', models.TextField(default='')),
                ('visible', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebVR.Project')),
            ],
            options={
                'abstract': False,
            },
            bases=('WebVR.shadow', 'WebVR.rotation', 'WebVR.position', 'WebVR.scale'),
        ),
        migrations.CreateModel(
            name='a_sphere',
            fields=[
                ('scale_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.scale')),
                ('position_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.position')),
                ('rotation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.rotation')),
                ('shadow_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='WebVR.shadow')),
                ('name', models.CharField(max_length=50)),
                ('color', colorful.fields.RGBColorField(default=['#FF0000', '#00FF00', '#0000FF'])),
                ('src', models.TextField(default='')),
                ('visible', models.BooleanField(default=False)),
                ('height', models.FloatField(verbose_name=256)),
                ('radius', models.FloatField(verbose_name=1)),
                ('theta_length', models.FloatField(default=180)),
                ('theta_start', models.FloatField(default=0)),
                ('width', models.FloatField(default=512)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebVR.Project')),
            ],
            options={
                'abstract': False,
            },
            bases=('WebVR.shadow', 'WebVR.rotation', 'WebVR.position', 'WebVR.scale'),
        ),
    ]
