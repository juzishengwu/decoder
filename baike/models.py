#coding=utf-8
from django.db import models

class Snp(models.Model):
    rsid = models.CharField(max_length=100, unique=True)
    
    chromosome = models.CharField(max_length=10, default='', verbose_name=u'染色体')
    orientation = models.CharField(max_length=10, default='', verbose_name=u'正向链 or 反向链')
    position = models.CharField(max_length=10, default='', verbose_name=u'染色体上位置')
    gene = models.CharField(max_length=100, default='', verbose_name=u'基因')
    summary = models.CharField(max_length=500, default='', blank=True)
    summary_cn = models.CharField(max_length=500, default='', verbose_name=u'中文的summary', blank=True)
    description = models.TextField(default='', blank=True)
    description_cn = models.TextField(default='', verbose_name=u'中文的description',blank=True)
    
    magnitude = models.FloatField(default=0, verbose_name='重要性')
    
    def __unicode__(self):
        return 'rs%s'%self.rsid
        
repute_choices = (
    ('neutral', u'中性'),
    ('Good', u'有益'),
    ('Bad', u'有害'),
)
class Genotype(models.Model):
    class Meta:
        unique_together = (('snp', 'allele'),)

    snp = models.ForeignKey('Snp')
    allele1 = models.CharField(max_length=10, default='')
    allele2 = models.CharField(max_length=10, default='')
    allele = models.CharField(max_length=10, default='')
    allele_flipped = models.CharField(max_length=10, default='')
    magnitude = models.FloatField(default=0, verbose_name='重要性')
    repute = models.CharField(max_length=10, choices=repute_choices, default='neutral', verbose_name='good or bad', blank=True)
    summary = models.CharField(max_length=500, default='', blank=True)
    summary_cn = models.CharField(max_length=500, default='', verbose_name=u'中文的summary', blank=True)
    description = models.TextField(default='', blank=True)
    description_cn = models.TextField(default='', verbose_name=u'中文的description', blank=True)

    def __unicode__(self):
        return 'rs%s(%s:%s)'%(self.snp.rsid, self.allele1, self.allele2)
