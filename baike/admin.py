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

admin.site.register(Snp, SnpAdmin)
admin.site.register(Genotype, GenotypeAdmin)
