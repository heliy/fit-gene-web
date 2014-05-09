# encoding:utf-8

from django.db import models

# 染色体最多碱基对 
class Chr_len(models.Model):
    chr_no = models.CharField("Chr #",max_length=2)
    max_len = models.IntegerField()

    def __unicode___(self):
        return self.chr_no

# 基因信息 
class Gene(models.Model):
    entrez = models.CharField("entrez ID",max_length=20)
    symbol = models.CharField("Gene Symbol",max_length=20)
    chr_no = models.CharField("Chr #",max_length=2)
    loc_begin = models.IntegerField("Begin")
    loc_end = models.IntegerField("End")

    def __unicode__(self):
        return self.symbol
