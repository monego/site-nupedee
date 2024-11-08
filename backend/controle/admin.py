import django_filters
from django.contrib import admin
from django.contrib.auth.models import User
from controle.models import (
    Ausencia,
    ControleAcesso,
    Emprestimo,
    Equipamento,
    HorarioTrabalho,
    ItemEmprestimo,
    Manutencao,
)

class AusenciaAdmin(admin.ModelAdmin):
    list_display = ('funcionario', 'inicio', 'fim', 'motivo')
    search_fields = ('funcionario',)

class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'foto', 'manual')
    search_fields = ('nome', 'descricao')

class EmprestimosAdmin(admin.ModelAdmin):
    list_display = ('responsavel', 'funcionario', 'local', 'retirada', 'devolucao')
    search_fields = ('responsavel', 'local')

class HorarioTrabalhoAdmin(admin.ModelAdmin):
    list_display = (
        'funcionario',
        'dia_da_semana',
        'inicio',
        'fim',
        'inicio_intervalo',
        'fim_intervalo',
    )
    search_fields = ('funcionario',)

class ItemEmprestimoAdmin(admin.ModelAdmin):
    list_display = ('emprestimo', 'equipamento', 'nome')

class ManutencaoAdmin(admin.ModelAdmin):
    list_display = ('equipamento', 'funcionario', 'descricao', 'data')
    search_fields = ('equipamento', 'funcionario')

class ControleAcessoAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'sala')

admin.site.register(Ausencia, AusenciaAdmin)
admin.site.register(ControleAcesso, ControleAcessoAdmin)
admin.site.register(Emprestimo, EmprestimosAdmin)
admin.site.register(Equipamento, EquipamentoAdmin)
admin.site.register(HorarioTrabalho, HorarioTrabalhoAdmin)
admin.site.register(ItemEmprestimo, ItemEmprestimoAdmin)
admin.site.register(Manutencao, ManutencaoAdmin)
