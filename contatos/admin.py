from django.contrib import admin
from .models import Contato, Categoria


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'categoria', 'mostrar')
    list_editable = ('mostrar', 'telefone')
    list_dislpay_links = ('nome', 'sobrenome')
    list_filter = ('categoria', 'mostrar')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'telefone')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
