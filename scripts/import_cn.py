#coding=utf-8
import os,re
os.environ['DJANGO_SETTINGS_MODULE'] = 'decoder.settings'
import django
django.setup()
from baike.models import *

data = open('cn.txt').read().split('\n')
iterator = iter(data)
while True:
    try:
        t = iterator.next()
        s = iterator.next()
        d = iterator.next()
    except StopIteration:
        break

    data = t.split(':')
    if len(data) == 2:
        rsid = data[1]
        snp = Snp.objects.get(rsid=rsid)
        snp.summary_cn = s
        snp.description_cn = d
        snp.save()
    if len(data) == 3:
        rsid = data[1]
        allele = data[2]
        snp = Snp.objects.get(rsid=rsid)
        g = snp.genotype_set.get(allele=allele)
        g.summary_cn = s
        g.description_cn = d
        g.save()

