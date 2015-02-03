#coding=utf-8
import sys, os
import mwparserfromhell

def parse(rsfn):
    wikicode = mwparserfromhell.parse(open(rsfn).read())
    t = wikicode.filter_templates()[0]

    rs = {}
    if t.name.strip() == 'Rsnum':
        for key in ['rsid','Gene', 'Chromosome', 'position', 'Orientation', 'Summary']:
            try:
                value = t.get(key)
                value = value.strip().split('=')[-1]
            except ValueError:
                continue
            else:
                rs[key.lower()] = value
    return rs 

if __name__ == '__main__':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'decoder.settings'
    import django
    django.setup()
    from baike.models import Snp
    from django.db import IntegrityError

    a = sys.argv[1]
    if os.path.isfile(a):
        r = parse(a)
        if r:
            Snp.objects.create(**r)

    if os.path.isdir(a):
        for fn in os.listdir(a):
            if fn.startswith('Rs'):# and fn.endswith('txt'):
                rsfn = os.path.join(a, fn)
                print rsfn
                r = parse(rsfn)
                if not r:continue
                try:
                    Snp.objects.create(**r)
                except IntegrityError:
                    print 'duplicate %s'%r['rsid']
                    continue
