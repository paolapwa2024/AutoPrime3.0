from django import forms
from .models import Veiculo, OrdemServico


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['cliente', 'marca', 'modelo', 'placa', 'ano']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        fields = ['cliente', 'veiculo', 'problema_relatado', 'status', 'aprovado_cliente']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'veiculo': forms.Select(attrs={'class': 'form-select'}),
            'problema_relatado': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'aprovado_cliente': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

from .models import (
    Veiculo, OrdemServico, Cliente, Diagnostico, Servico, Pagamento
)


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'email']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = ['ordem_servico', 'mecanico_responsavel', 'problema_encontrado']
        widgets = {
            'ordem_servico': forms.Select(attrs={'class': 'form-select'}),
            'mecanico_responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'problema_encontrado': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['ordem_servico', 'descricao', 'valor', 'status']
        widgets = {
            'ordem_servico': forms.Select(attrs={'class': 'form-select'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }


class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['ordem_servico', 'valor_final', 'forma_pagamento', 'data_entrega']
        widgets = {
            'ordem_servico': forms.Select(attrs={'class': 'form-select'}),
            'valor_final': forms.NumberInput(attrs={'class': 'form-control'}),
            'forma_pagamento': forms.Select(attrs={'class': 'form-select'}),
            'data_entrega': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }