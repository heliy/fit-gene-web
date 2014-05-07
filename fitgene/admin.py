from django.contrib import admin
from fitgene.models import Chr_len,Gene

class ChrAdmin(admin.ModelAdmin):
    fileds = ['chr_no', 'max_len']
    list_display = ('chr_no','max_len')

class GeneAdmin(admin.ModelAdmin):
    list_diaplay = ('entrez','symbol','chr_no','loc_begin','loc_end')
    
admin.site.register(Chr_len,ChrAdmin)
admin.site.register(Gene,GeneAdmin)
