#coding=utf-8
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'manu2.settings'
import django
django.setup()
from snpedia.models import *
n = 0
for snp in Snp.objects.order_by('-magnitude'):
    print snp.rsid, snp.magnitude
    if snp.summary:
        print 'summary:', snp.summary.encode('u8')
        n += len(snp.summary)
    if snp.description:
        print 'description:', snp.description.encode('u8')
        n += len(snp.description)
        
    for geno in snp.genotype_set.all():
        print geno.allele, geno.magnitude, geno.repute
        if geno.summary:
            print 'summary:', geno.summary.encode('u8')
            n += len(snp.summary)
        if geno.description:
            print 'description:', geno.description.encode('u8')
            n += len(snp.description)
    print

print n
