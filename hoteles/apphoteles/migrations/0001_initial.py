# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogoServicios',
            fields=[
            ],
            options={
                'db_table': 'catalogo_servicios',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
            ],
            options={
                'db_table': 'ciudad',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
            ],
            options={
                'db_table': 'contacto',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fotos',
            fields=[
            ],
            options={
                'db_table': 'fotos',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
            ],
            options={
                'db_table': 'habitacion',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
            ],
            options={
                'db_table': 'hotel',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Promocion',
            fields=[
            ],
            options={
                'db_table': 'promocion',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
            ],
            options={
                'db_table': 'provincia',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
            ],
            options={
                'db_table': 'servicios',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
