from django.contrib import admin
from .models import (
    Cliente, Veiculo, OrdemServico, Diagnostico, Servico, Pagamento
)


admin.site.register(Cliente)
admin.site.register(Veiculo)


class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'veiculo', 'cliente', 'status', 'data_criacao')
    list_filter = ('status',)
    search_fields = ('veiculo__placa', 'cliente__nome')


admin.site.register(OrdemServico, OrdemServicoAdmin)
admin.site.register(Diagnostico)


class ServicoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'ordem_servico', 'status', 'valor')
    list_filter = ('status',)


admin.site.register(Servico, ServicoAdmin)
admin.site.register(Pagamento)