from django.core.management.base import BaseCommand
from veiculos.models import (
    Cliente, Veiculo, OrdemServico, Diagnostico, Servico, Pagamento
)


class Command(BaseCommand):
    help = 'Popula o banco com clientes, veículos e ordens de serviço de teste'

    def handle(self, *args, **options):
        clientes_dados = [
            {'nome': 'Ana Souza', 'telefone': '(21) 98888-1111', 'email': 'ana@email.com'},
            {'nome': 'Bruno Lima', 'telefone': '(21) 98888-2222', 'email': 'bruno@email.com'},
            {'nome': 'Carla Mendes', 'telefone': '(21) 98888-3333', 'email': 'carla@email.com'},
            {'nome': 'Diego Alves', 'telefone': '(21) 98888-4444', 'email': 'diego@email.com'},
            {'nome': 'Elaine Rocha', 'telefone': '(21) 98888-5555', 'email': 'elaine@email.com'},
        ]

        veiculos_dados = [
            {'marca': 'Honda', 'modelo': 'Civic', 'placa': 'ABC1A11', 'ano': 2020},
            {'marca': 'Toyota', 'modelo': 'Corolla', 'placa': 'BCD2B22', 'ano': 2021},
            {'marca': 'Volkswagen', 'modelo': 'Gol', 'placa': 'CDE3C33', 'ano': 2018},
            {'marca': 'Chevrolet', 'modelo': 'Onix', 'placa': 'DEF4D44', 'ano': 2022},
            {'marca': 'Fiat', 'modelo': 'Argo', 'placa': 'EFG5E55', 'ano': 2019},
        ]

        clientes = []
        for dados in clientes_dados:
            cliente, _ = Cliente.objects.get_or_create(
                nome=dados['nome'],
                defaults={'telefone': dados['telefone'], 'email': dados['email']}
            )
            clientes.append(cliente)
            self.stdout.write(self.style.SUCCESS(f'Cliente: {cliente.nome}'))

        veiculos = []
        for i, dados in enumerate(veiculos_dados):
            veiculo, _ = Veiculo.objects.get_or_create(
                placa=dados['placa'],
                defaults={
                    'cliente': clientes[i],
                    'marca': dados['marca'],
                    'modelo': dados['modelo'],
                    'ano': dados['ano'],
                }
            )
            veiculos.append(veiculo)
            self.stdout.write(self.style.SUCCESS(f'Veículo: {veiculo}'))

        os1, _ = OrdemServico.objects.get_or_create(
            veiculo=veiculos[0],
            cliente=clientes[0],
            problema_relatado='Barulho estranho no motor ao acelerar',
            defaults={'status': 'entregue', 'aprovado_cliente': True}
        )
        Diagnostico.objects.get_or_create(
            ordem_servico=os1,
            defaults={
                'mecanico_responsavel': 'João Mecânico',
                'problema_encontrado': 'Correia dentada desgastada',
            }
        )
        Servico.objects.get_or_create(
            ordem_servico=os1,
            descricao='Troca da correia dentada',
            defaults={'valor': 450.00, 'status': 'concluido'}
        )
        Pagamento.objects.get_or_create(
            ordem_servico=os1,
            defaults={'valor_final': 450.00, 'forma_pagamento': 'pix'}
        )

        os2, _ = OrdemServico.objects.get_or_create(
            veiculo=veiculos[1],
            cliente=clientes[1],
            problema_relatado='Freios fazendo barulho',
            defaults={'status': 'manutencao', 'aprovado_cliente': True}
        )
        Diagnostico.objects.get_or_create(
            ordem_servico=os2,
            defaults={
                'mecanico_responsavel': 'Maria Mecânica',
                'problema_encontrado': 'Pastilhas de freio gastas',
            }
        )
        Servico.objects.get_or_create(
            ordem_servico=os2,
            descricao='Troca das pastilhas de freio',
            defaults={'valor': 280.00, 'status': 'andamento'}
        )
        Pagamento.objects.get_or_create(
            ordem_servico=os2,
            defaults={'valor_final': 280.00, 'forma_pagamento': 'cartao_credito'}
        )

        os3, _ = OrdemServico.objects.get_or_create(
            veiculo=veiculos[2],
            cliente=clientes[2],
            problema_relatado='Ar-condicionado não gela',
            defaults={'status': 'aguardando_aprovacao', 'aprovado_cliente': False}
        )
        Diagnostico.objects.get_or_create(
            ordem_servico=os3,
            defaults={
                'mecanico_responsavel': 'João Mecânico',
                'problema_encontrado': 'Gás do ar-condicionado insuficiente',
            }
        )
        Servico.objects.get_or_create(
            ordem_servico=os3,
            descricao='Recarga de gás do ar-condicionado',
            defaults={'valor': 220.00, 'status': 'aguardando'}
        )
        Pagamento.objects.get_or_create(
            ordem_servico=os3,
            defaults={'valor_final': 220.00, 'forma_pagamento': 'dinheiro'}
        )

        os4, _ = OrdemServico.objects.get_or_create(
            veiculo=veiculos[3],
            cliente=clientes[3],
            problema_relatado='Revisão dos 20 mil km',
            defaults={'status': 'aberta', 'aprovado_cliente': False}
        )
        Diagnostico.objects.get_or_create(
            ordem_servico=os4,
            defaults={
                'mecanico_responsavel': 'Maria Mecânica',
                'problema_encontrado': 'Aguardando avaliação inicial',
            }
        )
        Servico.objects.get_or_create(
            ordem_servico=os4,
            descricao='Revisão completa dos 20 mil km',
            defaults={'valor': 350.00, 'status': 'aguardando'}
        )
        Pagamento.objects.get_or_create(
            ordem_servico=os4,
            defaults={'valor_final': 350.00, 'forma_pagamento': 'cartao_debito'}
        )

        os5, _ = OrdemServico.objects.get_or_create(
            veiculo=veiculos[4],
            cliente=clientes[4],
            problema_relatado='Troca de óleo e filtros',
            defaults={'status': 'pronto', 'aprovado_cliente': True}
        )
        Diagnostico.objects.get_or_create(
            ordem_servico=os5,
            defaults={
                'mecanico_responsavel': 'João Mecânico',
                'problema_encontrado': 'Óleo e filtro vencidos pelo tempo de uso',
            }
        )
        Servico.objects.get_or_create(
            ordem_servico=os5,
            descricao='Troca de óleo e filtro de óleo',
            defaults={'valor': 180.00, 'status': 'concluido'}
        )
        Pagamento.objects.get_or_create(
            ordem_servico=os5,
            defaults={'valor_final': 180.00, 'forma_pagamento': 'pix'}
        )

        self.stdout.write(self.style.SUCCESS('Dados de teste criados com sucesso!'))