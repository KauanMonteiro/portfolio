from django.contrib import admin
from .models import Projeto,Category

class ProjetoAdmin(admin.ModelAdmin):
    # Display specific fields in the list view
    list_display = ('titulo', 'link', 'github')

    # Make it searchable by the specified fields
    search_fields = ('titulo', 'descricao', 'github','category')

    # Define the form layout in the admin
    fieldsets = (
        (None, {
            'fields': ('titulo', 'descricao', 'link', 'github','category')
        }),
        ('Imagens/Vídeos', {
            'fields': ('capa_img', 'capa_video')
        }),
        ('Executáveis', {
            'fields': ('exe', 'linux', 'apk')
        }),
    )

    list_filter = ('titulo', 'github') 

    list_per_page = 20 
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Category)