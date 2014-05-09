import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "..loc_fit_gene.settings")

from fitgene.models import Chr_len,Gene
from django.db.models import Q

def action_context(chr_no,loc,display):
    context={'genes':None,'fit':None,'chr_no':chr_no.upper(),'loc':loc,'display':display,'statu':None}
    chr=Chr_len.objects.filter(chr_no=context['chr_no'])
    if len(chr)==0:
        context['statu']='chr'
        return context
    max_len=chr[0].max_len
    if not loc.isdigit():
        context['statu']='loc'
        return context
    loc=int(loc)
    if loc>max_len:
        context['statu']='beyond'
        return context
    if not display.isdigit():
        context['statu']='display'
        return context
    dis=int(display)
    fr=loc-dis
    to=loc+dis
    context['genes']=Gene.objects.filter(Q(loc_begin__lte=fr)|Q(loc_end__gte=to))
    for gene in context['genes']:
        if gene.loc_begin <= loc and gene.loc_end >= loc:
            context['fit']=gene
    if context['fit']==None:
        context['statu']='unfit'
        return context
    else:
        context['statu']='fit'
        return context
    
