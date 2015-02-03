#coding=utf-8
import os,sys,time,argparse,shutil
os.environ['DJANGO_SETTINGS_MODULE'] = 'decoder.settings'
import django
django.setup()
from django.template import *
from baike.models import *

def equal(a, b):
    a = a.upper()
    b = b.upper()

    if len(a) != 2 or len(b) != 2:
        return False
    
    if a == b: return True
    c = '%s%s'%(a[1], a[0])
    if c == b: return True
    
    return False

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, help=u"基因文件")
parser.add_argument("-t", "--report_type", type=str, default='html', help=u"报告的类型:文本文件(-t txt);网页(-t html)")
parser.add_argument("-o", "--output", type=str, default='report', help=u"报告的生成目录(-t html) or  报告文件名(-t txt)")
#parser.add_argument("-l", "--language", type=str, default='en', help=u"报告的语言:中文(-l cn);英文(-l en)")
args = parser.parse_args()

input_ = args.input
output = args.output

data = {}
for line in file(input_):
    if line.startswith('#'):continue
    line = line.strip()
    rsid = line.split('\t')[0].lower()
    geno = line.split('\t')[-1]
    data[rsid] = geno

matched = []
for g in Genotype.objects.order_by('-magnitude').all():
    s = g.snp
    rsid = 'rs%s'%s.rsid
    if equal(data.get(rsid, ''), g.allele_flipped):
        matched.append(g)

if args.report_type == 'txt':
    
    if not args.output.endswith('txt'):
        output_fn = '%s.txt'%args.output
    else:
        output_fn = args.output
    fn = open(output_fn, 'w')
    headers = ['RSID', 'Allele', 'magnitude', 'repute', 'chromosome', 'position', 'gene', 'summary_en', 'summary_cn']
    fn.write('\t'.join(headers))
    fn.write('\n')

    for g in matched:
        s = g.snp
        rsid = 'rs%s'%s.rsid
        line = [rsid.upper(), data[rsid], g.magnitude, g.repute, s.chromosome, s.position, s.gene, g.summary.encode('u8'), g.summary_cn.encode('u8')]
        line = [str(i) for i in line]
        fn.write('\t'.join(line))
        fn.write('\n')
    fn.close()

if args.report_type == 'html':
    shutil.copytree('report_template', args.output)

    fn_cn = os.path.join(args.output, 'report_cn.html')
    t =  Template(open('report_template/template_cn.html').read())
    c = Context({'matched': matched})
    s = t.render(c).encode('u8')
    open(fn_cn, 'w').write(s)

    fn_en = os.path.join(args.output, 'report.html')
    t =  Template(open('report_template/template_en.html').read())
    c = Context({'matched': matched})
    s = t.render(c).encode('u8')
    open(fn_en, 'w').write(s)
    
    t1 = os.path.join(args.output, 'template_cn.html')
    os.remove(t1)
    t2 = os.path.join(args.output, 'template_en.html')
    os.remove(t2)
