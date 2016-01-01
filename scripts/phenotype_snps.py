#coding=utf-8
import os,sys,argparse
os.environ['DJANGO_SETTINGS_MODULE'] = 'decoder.settings'
import django
django.setup()
from baike.models import *

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--id", type=str, help=u"表型数据id")
parser.add_argument("-s", "--snps", type=str, help=u"相关snps的rsid")
parser.add_argument("-a", "--action", default='add', type=str, help=u"关联or去除关联")

args = parser.parse_args()
phenotype = Phenotype.objects.get(id=args.id)
sids = args.snps.split(',')

for sid in sids:
    sid = sid.lower()
    if sid.startswith('rs'):
        sid = sid[2:]
    if args.action == 'add':
        snp, is_created = Snp.objects.get_or_create(rsid=sid)
        if is_created:
            print snp, 'created.'
        phenotype.snps.add(snp)
    if args.action == 'delete':
        try:
            snp = Snp.objects.get(rsid=sid)
        except Snp.DoesNotExist,e:
            pass
        else:
            phenotype.snps.remove(snp)
