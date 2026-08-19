from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name='veiculos'
    )
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    placa = models.CharField(max_length=10, unique=True)
    ano = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.marca} {self.modelo} - {self.placa}'


class OrdemServico(models.Model):
    STATUS_CHOICES = [
        ('aberta', 'Aberta'),
        ('diagnostico', 'Em diagnóstico'),
        ('orcamento', 'Orçamento enviado'),
        ('aguardando_aprovacao', 'Aguardando aprovação'),
        ('manutencao', 'Em manutenção'),
        ('conferencia', 'Em conferência'),
        ('pronto', 'Pronto para retirada'),
        ('entregue', 'Entregue'),
    ]

    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name='ordens_servico'
    )
    veiculo = models.ForeignKey(
        Veiculo, on_delete=models.CASCADE, related_name='ordens_servico'
    )
    problema_relatado = models.TextField()
    status = models.CharField(
        max_length=30, choices=STATUS_CHOICES, default='aberta'
    )
    aprovado_cliente = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'OS #{self.id} - {self.veiculo}'


class Diagnostico(models.Model):
    ordem_servico = models.OneToOneField(
        OrdemServico, on_delete=models.CASCADE, related_name='diagnostico'
    )
    mecanico_responsavel = models.CharField(max_length=100)
    problema_encontrado = models.TextField()
    data_diagnostico = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Diagnóstico da {self.ordem_servico}'


class Servico(models.Model):
    STATUS_CHOICES = [
        ('aguardando', 'Aguardando'),
        ('andamento', 'Em andamento'),
        ('concluido', 'Concluído'),
    ]

    ordem_servico = models.ForeignKey(
        OrdemServico, on_delete=models.CASCADE, related_name='servicos'
    )
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='aguardando'
    )

    def __str__(self):
        return f'{self.descricao} - {self.get_status_display()}'


class Pagamento(models.Model):
    FORMA_PAGAMENTO_CHOICES = [
        ('dinheiro', 'Dinheiro'),
        ('pix', 'Pix'),
        ('cartao_credito', 'Cartão de Crédito'),
        ('cartao_debito', 'Cartão de Débito'),
    ]

    ordem_servico = models.OneToOneField(
        OrdemServico, on_delete=models.CASCADE, related_name='pagamento'
    )
    valor_final = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(
        max_length=20, choices=FORMA_PAGAMENTO_CHOICES
    )
    data_entrega = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Pagamento da {self.ordem_servico}'