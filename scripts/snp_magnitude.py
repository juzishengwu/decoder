#coding=utf-8
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'manu2.settings'
import django
django.setup()
from snpedia.models import *

for snp in Snp.objects.all():
    ms = [g.magnitude for g in snp.genotype_set.all()]
    if ms:
        print snp.rsid
        snp.magnitude = max(ms)
        snp.save()
