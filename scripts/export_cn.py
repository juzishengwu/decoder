#coding=utf-8
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'manu2.settings'
import django
django.setup()
from snpedia.models import *

for snp in Snp.objects.all():
    print 'snp'
    print snp.rsid
    print snp.summary_cn
    print snp.description_cn
    for geno in snp.genotype_set.all():
        print geno.allele
        print geno.summary_cn
        print description_cn
