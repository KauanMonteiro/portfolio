from django.contrib import admin
from .models import Projeto

class ProjetoAdmin(admin.ModelAdmin):
    # Display specific fields in the list view
    list_display = ('titulo', 'link', 'github')

    # Make it searchable by the specified fields
    search_fields = ('titulo', 'descricao', 'github')

    # Define the form layout in the admin
    fieldsets = (
        (None, {
            'fields': ('titulo', 'descricao', 'link', 'github')
        }),
        ('Imagens/Vídeos', {
            'fields': ('capa_img', 'capa_video')
        }),
        ('Executáveis', {
            'fields': ('exe', 'linux', 'apk')
        }),
    )

    # Customize the way the admin handles the list view
    list_filter = ('titulo', 'github')  # You can filter by fields in the admin

    # Enable pagination in the admin list view
    list_per_page = 20  # Number of items to show per page in list view

# Register the Projeto model with the customized admin class
admin.site.register(Projeto, ProjetoAdmin)
