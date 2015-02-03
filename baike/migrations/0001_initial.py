# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genotype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allele1', models.CharField(default=b'', max_length=10)),
                ('allele2', models.CharField(default=b'', max_length=10)),
                ('allele', models.CharField(default=b'', max_length=10)),
                ('magnitude', models.FloatField(default=0, verbose_name=b'\xe9\x87\x8d\xe8\xa6\x81\xe6\x80\xa7')),
                ('repute', models.CharField(default=b'neutral', max_length=10, verbose_name=b'good or bad', blank=True, choices=[(b'neutral', '\u4e2d\u6027'), (b'good', '\u6709\u76ca'), (b'bad', '\u6709\u5bb3')])),
                ('summary', models.CharField(default=b'', max_length=500, blank=True)),
                ('summary_cn', models.CharField(default=b'', max_length=500, verbose_name='\u4e2d\u6587\u7684summary', blank=True)),
                ('description', models.TextField(default=b'', blank=True)),
                ('description_cn', models.TextField(default=b'', verbose_name='\u4e2d\u6587\u7684description', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Snp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rsid', models.CharField(unique=True, max_length=100)),
                ('chromosome', models.CharField(default=b'', max_length=10, verbose_name='\u67d3\u8272\u4f53')),
                ('orientation', models.CharField(default=b'', max_length=10, verbose_name='\u6b63\u5411\u94fe or \u53cd\u5411\u94fe')),
                ('position', models.CharField(default=b'', max_length=10, verbose_name='\u67d3\u8272\u4f53\u4e0a\u4f4d\u7f6e')),
                ('gene', models.CharField(default=b'', max_length=100, verbose_name='\u57fa\u56e0')),
                ('summary', models.CharField(default=b'', max_length=500, blank=True)),
                ('summary_cn', models.CharField(default=b'', max_length=500, verbose_name='\u4e2d\u6587\u7684summary', blank=True)),
                ('description', models.TextField(default=b'', blank=True)),
                ('description_cn', models.TextField(default=b'', verbose_name='\u4e2d\u6587\u7684description', blank=True)),
                ('magnitude', models.FloatField(default=0, verbose_name=b'\xe9\x87\x8d\xe8\xa6\x81\xe6\x80\xa7')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='genotype',
            name='snp',
            field=models.ForeignKey(to='baike.Snp'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='genotype',
            unique_together=set([('snp', 'allele')]),
        ),
    ]
