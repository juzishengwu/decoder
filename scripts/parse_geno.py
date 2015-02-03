#coding=utf-8
import os, sys
import mwparserfromhell

def parse(genofn):
    fn = genofn
    wikicode = mwparserfromhell.parse(open(fn).read())
    ts = wikicode.filter_templates()
    if not ts:
        return {}
    t = ts[0]

    geno = {}
    if t.name.strip() == 'Genotype':
        for key in ['rsid', 'allele1','allele2', 'magnitude', 'repute', 'summary']:
            try:
                value = t.get(key)
                value = value.strip().split('=')[-1]
            except ValueError:
                continue
            else:
                geno[key.lower()] = value
    
    if not geno.get('rsid', ''):
        return {}
    
    if not geno.get('magnitude', ''): 
        geno['magnitude'] = 0
    else:
        try:
            geno['magnitude'] = float(geno['magnitude'])
        except ValueError:
            geno['magnitude'] = 0

    return geno

if __name__ == '__main__':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'decoder.settings'
    import django
    django.setup()
    from django.db import IntegrityError
    from baike.models import *
    
    def geno2db(geno):
        rsid = geno['rsid']
        try:
            snp = Snp.objects.get(rsid=rsid)
        except  Snp.DoesNotExist:
            print 'no snp %s'%rsid
            return
        
        geno.pop('rsid')
        geno['allele'] = geno.get('allele1', '') + geno.get('allele2', '')
        
        if not geno['allele']:
            print 'no allele %s'%rsid
            return

        try:
            g = Genotype(**geno)
            #print snp
            #print geno['allele']
            g.snp = snp
            g.save()
        except IntegrityError, e:
            print e
            print geno

    a = sys.argv[1]
    if os.path.isfile(a):
        r = parse(a)
        if r:geno2db(r)

    if os.path.isdir(a):
        for fn in os.listdir(a):
            if fn.startswith('Rs') and fn.endswith('txt'):
                genofn = os.path.join(a, fn)
                print genofn
                r = parse(genofn)
                if r:
                    geno2db(r)
