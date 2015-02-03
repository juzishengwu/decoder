#coding=utf-8
#http://www.snpedia.com/index.php/Orientation
#https://customercare.23andme.com/hc/en-us/articles/202907660-Which-DNA-strand-does-23andMe-report-for-SNP-genotypes

import os,sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'decoder.settings'
import django
django.setup()
from baike.models import *

def flip(s):
    orientatio_map = {'A': 'T',
                      'T': 'A',
                      'G': 'C',
                      'C': 'G'}
    r = []
    for i in s:
        try:
            r.append(orientatio_map[i.upper()])
        except KeyError:
            return s
    return ''.join(r)
        
for g in Genotype.objects.all():
    if g.snp.orientation == 'plus':
        g.allele_flipped = g.allele
        g.save()
    
    if g.snp.orientation == 'minus':
        g.allele_flipped = flip(g.allele)
        g.save()
