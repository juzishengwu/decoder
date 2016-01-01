#coding=utf-8
from django.db import models

class Snp(models.Model):
    rsid = models.CharField(max_length=100, unique=True)

    chromosome = models.CharField(max_length=10, default='', blank=True, verbose_name=u'染色体')
    orientation = models.CharField(max_length=10, default='', blank=True, verbose_name=u'正向链 or 反向链')
    position = models.CharField(max_length=10, default='', blank=True, verbose_name=u'染色体上位置')
    gene = models.CharField(max_length=100, default='', blank=True, verbose_name=u'基因')
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
    allele_flipped = models.CharField(max_length=10, default='', blank=True)
    magnitude = models.FloatField(default=0, verbose_name='重要性', blank=True)
    repute = models.CharField(max_length=10, choices=repute_choices, default='neutral', verbose_name='good or bad', blank=True)
    summary = models.CharField(max_length=500, default='', blank=True)
    summary_cn = models.CharField(max_length=500, default='', verbose_name=u'中文的summary', blank=True)
    summary2 = models.CharField(max_length=500, default='', blank=True)
    summary2_cn = models.CharField(max_length=500, default='', verbose_name=u'中文的summary2', blank=True)
    description = models.TextField(default='', blank=True)
    description_cn = models.TextField(default='', verbose_name=u'中文的description', blank=True)

    def __unicode__(self):
        return 'rs%s(%s:%s)'%(self.snp.rsid, self.allele1, self.allele2)

phenotype_category_choices = (
    ('nutrition_metabolism', u'营养代谢'),
    ('genetic_characteristics', u'遗传特征'),
    ('health_risk', u'健康风险'),
    ('genetic_diseases', u'遗传性疾病'),
    ('drug_reactions', u'药物反应'),
    ('sports', u'运动基因'),
    ('ancestry', u'祖源'),
)

class Phenotype(models.Model):
    name = models.CharField(max_length=250)
    name_cn = models.CharField(max_length=250, default='', verbose_name=u'名称', blank=True)

    #pic = models.ImageField()

    intro = models.TextField(default='', blank=True)
    intro_cn = models.TextField(default='', blank=True, verbose_name=u'简介')
    intro2 = models.TextField(default='', blank=True)
    intro2_cn = models.TextField(default='', blank=True, verbose_name=u'简介2')

    description = models.TextField(default='', blank=True)
    description_cn = models.TextField(default='', verbose_name=u'描述', blank=True)
    description2 = models.TextField(default='', blank=True)
    description2_cn = models.TextField(default='', verbose_name=u'描述2', blank=True)

    category = models.CharField(max_length=40, choices=phenotype_category_choices,
                                verbose_name='类别', blank=True)

    prevalence_floor = models.DecimalField(max_digits=20, decimal_places=18, blank=True, null=True)
    prevalence_ceil = models.DecimalField(max_digits=20, decimal_places=18, blank=True, null=True)
    prevalence_rate = models.DecimalField(max_digits=20, decimal_places=18, blank=True, null=True)
    prevalence_rate2 = models.IntegerField(blank=True, null=True, verbose_name=u'发生率（单位：/10万人）')
    prevalence = models.TextField(default='', blank=True)
    prevalence_cn = models.TextField(default='', verbose_name=u'患病率', blank=True)
    prevalence2 = models.TextField(default='', blank=True)
    prevalence2_cn = models.TextField(default='', verbose_name=u'患病率2', blank=True)

    pathogenesis = models.TextField(default='', blank=True)
    pathogenesis_cn = models.TextField(default='', blank=True, verbose_name=u'病因')
    pathogenesis2 = models.TextField(default='', blank=True)
    pathogenesis2_cn = models.TextField(default='', blank=True, verbose_name=u'病因2')

    precaution = models.TextField(default='', blank=True)
    precaution_cn = models.TextField(default='', blank=True, verbose_name=u'预防措施')
    precaution2 = models.TextField(default='', blank=True)
    precaution2_cn = models.TextField(default='', blank=True, verbose_name=u'预防措施2')

    therapy = models.TextField(default='', blank=True)
    therapy_cn = models.TextField(default='', blank=True, verbose_name=u'治疗方案')
    therapy2 = models.TextField(default='', blank=True)
    therapy2_cn = models.TextField(default='', blank=True, verbose_name=u'治疗方案2')

    snps = models.ManyToManyField('Snp', blank=True)

    def __unicode__(self):
        return "%s (%s)"%(self.name, self.name_cn)
