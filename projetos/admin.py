from django.contrib import admin
from .models import Projeto

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo','link', 'github')
    
    search_fields = ('titulo', 'descricao', 'github')
    


    fieldsets = (
        (None, {
            'fields': ('titulo', 'descricao', 'link', 'github')
        }),
        ('Imagens/Vídeos', {
            'fields': ('capa_img', 'capa_video') 
        }),
        ('Executáveis', {
            'fields': ('executaveis',)
        }),
    )


admin.site.register(Projeto, ProjetoAdmin)
