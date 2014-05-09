import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "..loc_fit_gene.settings")

from fitgene.models import Chr_len,Gene
from django.db.models import Q

def action_context(chr_no,loc):
    context={'fit':None,'chr_no':chr_no.upper(),'loc':loc,'statu':None}
    if len(chr_no)==0 or len(loc)==0:
        context['statu']='null'
        return context
    chrs=Chr_len.objects.filter(chr_no=context['chr_no'])
    if len(chrs)==0:
        context['statu']='chr'
        return context
    max_len=chrs[0].max_len
    if not loc.isdigit():
        context['statu']='loc'
        return context
    loc=int(loc)
    if loc>max_len:
        context['display']=str(max_len)
        context['statu']='beyond'
        return context
    context['fit']=Gene.objects.filter(Q(chr_no=context['chr_no']),Q(loc_end__gte=loc),Q(loc_begin__lte=loc))
    if len(context['fit'])==0:
        context['statu']='unfit'
        return context
    else:
        context['fit']=context['fit'][0]
        context['statu']='fit'
        return context
    
