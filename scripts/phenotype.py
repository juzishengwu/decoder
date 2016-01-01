#coding=utf-8
import os,sys,argparse
os.environ['DJANGO_SETTINGS_MODULE'] = 'decoder.settings'
import django
django.setup()
from baike.models import *

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--id", type=str, help=u"表型数据id")
args = parser.parse_args()

p = Phenotype.objects.get(id=args.id)
print '%s(%s)\n'%(p.name, p.name_cn)
print p.intro, '\n'
print p.intro_cn, '\n'

print 'SNP:\n'
for snp in p.snps.all():
    print snp
    if snp.summary:
        print snp.summary
    if snp.summary_cn:
        print snp.summary_cn
    for g in snp.genotype_set.all():
        print g.allele, g.repute, g.magnitude
        if g.summary2:
            print g.summary2
        else:
            print g.summary
        if g.summary2_cn:
            print g.summary2_cn
        else:
            print g.summary_cn
    print
