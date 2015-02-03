#coding=utf-8
import os,sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'decoder.settings'
import django
django.setup()
from baike.models import *

fn = sys.argv[1]
for line in file(fn):
    if line.startswith('rs'):
        data = line.strip().split('\t')
        rsid = data[0]
        geno = data[-1]
        try:
            snp = Snp.objects.get(rsid=rsid[2:])
        except Snp.DoesNotExist:
            continue
        
        if snp.genotype_set.count() > 2:
            try:
                snp.genotype_set.get(allele=geno)
                print 'find it'
            except Genotype.DoesNotExist:
                print snp, geno

            
