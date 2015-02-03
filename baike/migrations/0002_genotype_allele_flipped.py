# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baike', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genotype',
            name='allele_flipped',
            field=models.CharField(default=b'', max_length=10),
            preserve_default=True,
        ),
    ]
