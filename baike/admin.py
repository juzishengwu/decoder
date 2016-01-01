#coding=utf-8
from django.contrib import admin
from baike.models import *

class GenoInline(admin.StackedInline):
    model = Genotype
    extra = 0

class SnpAdmin(admin.ModelAdmin):
    list_display = ('rsid', 'magnitude','chromosome', 'position', 'gene', 'summary')
    ordering = ('-magnitude', )
    search_fields = ('rsid', )
    inlines = [GenoInline]

class GenotypeAdmin(admin.ModelAdmin):
    pass

class PhenotypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_cn', 'category', 'prevalence_rate2')
    list_filter = ('category',)
admin.site.register(Snp, SnpAdmin)
admin.site.register(Genotype, GenotypeAdmin)
admin.site.register(Phenotype, PhenotypeAdmin)
