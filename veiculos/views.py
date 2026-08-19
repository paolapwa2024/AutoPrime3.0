from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Veiculo, OrdemServico
from .forms import VeiculoForm, OrdemServicoForm
from .models import (
    Veiculo, OrdemServico, Cliente, Diagnostico, Servico, Pagamento
)
from .forms import (
    VeiculoForm, OrdemServicoForm, ClienteForm, DiagnosticoForm,
    ServicoForm, PagamentoForm
)


def home(request):
    return render(request, 'home.html')


@login_required
def veiculo_list(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'veiculo_list.html', {'veiculos': veiculos})


@login_required
def veiculo_create(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('veiculo_list')
    else:
        form = VeiculoForm()
    return render(request, 'veiculo_form.html', {'form': form, 'titulo': 'Cadastrar Veículo'})


@login_required
def veiculo_update(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            return redirect('veiculo_list')
    else:
        form = VeiculoForm(instance=veiculo)
    return render(request, 'veiculo_form.html', {'form': form, 'titulo': 'Editar Veículo'})


@login_required
def veiculo_delete(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('veiculo_list')
    return render(request, 'veiculo_confirm_delete.html', {'veiculo': veiculo})


def veiculo_consulta(request):
    veiculo = None
    ordens_servico = None
    erro = None

    if request.method == 'POST':
        modelo = request.POST.get('modelo', '').strip()
        placa = request.POST.get('placa', '').strip().upper()

        try:
            veiculo = Veiculo.objects.get(
                modelo__iexact=modelo,
                placa__iexact=placa
            )
            ordens_servico = veiculo.ordens_servico.all()
        except Veiculo.DoesNotExist:
            erro = 'Nenhum veículo encontrado com esse modelo e placa. Verifique os dados.'

    return render(request, 'veiculo_consulta.html', {
        'veiculo': veiculo,
        'ordens_servico': ordens_servico,
        'erro': erro,
    })


@login_required
def os_list(request):
    ordens = OrdemServico.objects.all().order_by('-data_criacao')
    return render(request, 'os_list.html', {'ordens': ordens})


@login_required
def os_create(request):
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('os_list')
    else:
        form = OrdemServicoForm()
    return render(request, 'os_form.html', {'form': form, 'titulo': 'Nova Ordem de Serviço'})


@login_required
def os_update(request, pk):
    ordem = get_object_or_404(OrdemServico, pk=pk)
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST, instance=ordem)
        if form.is_valid():
            form.save()
            return redirect('os_list')
    else:
        form = OrdemServicoForm(instance=ordem)
    return render(request, 'os_form.html', {'form': form, 'titulo': 'Editar Ordem de Serviço'})


@login_required
def os_delete(request, pk):
    ordem = get_object_or_404(OrdemServico, pk=pk)
    if request.method == 'POST':
        ordem.delete()
        return redirect('os_list')
    return render(request, 'os_confirm_delete.html', {'ordem': ordem})

# --- Cliente ---
@login_required
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente_list.html', {'clientes': clientes})


@login_required
def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'form_generico.html', {
        'form': form, 'titulo': 'Cadastrar Cliente', 'cancel_url_name': 'cliente_list'
    })


@login_required
def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'form_generico.html', {
        'form': form, 'titulo': 'Editar Cliente', 'cancel_url_name': 'cliente_list'
    })


@login_required
def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'confirm_delete_generico.html', {
        'objeto': cliente, 'cancel_url_name': 'cliente_list', 'delete_url_name': 'cliente_delete'
    })


# --- Diagnostico ---
@login_required
def diagnostico_list(request):
    diagnosticos = Diagnostico.objects.all()
    return render(request, 'diagnostico_list.html', {'diagnosticos': diagnosticos})


@login_required
def diagnostico_create(request):
    if request.method == 'POST':
        form = DiagnosticoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diagnostico_list')
    else:
        form = DiagnosticoForm()
    return render(request, 'form_generico.html', {
        'form': form, 'titulo': 'Cadastrar Diagnóstico', 'cancel_url_name': 'diagnostico_list'
    })


@login_required
def diagnostico_update(request, pk):
    diagnostico = get_object_or_404(Diagnostico, pk=pk)
    if request.method == 'POST':
        form = DiagnosticoForm(request.POST, instance=diagnostico)
        if form.is_valid():
            form.save()
            return redirect('diagnostico_list')
    else:
        form = DiagnosticoForm(instance=diagnostico)
    return render(request, 'form_generico.html', {
        'form': form, 'titulo': 'Editar Diagnóstico', 'cancel_url_name': 'diagnostico_list'
    })


@login_required
def diagnostico_delete(request, pk):
    diagnostico = get_object_or_404(Diagnostico, pk=pk)
    if request.method == 'POST':
        diagnostico.delete()
        return redirect('diagnostico_list')
    return render(request, 'confirm_delete_generico.html', {
        'objeto': diagnostico, 'cancel_url_name': 'diagnostico_list', 'delete_url_name': 'diagnostico_delete'
    })


# --- Servico ---
@login_required
def servico_list(request):
    servicos = Servico.objects.all()
    return render(request, 'servico_list.html', {'servicos': servicos})


@login_required
def servico_create(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servico_list')
    else:
        form = ServicoForm()
    return render(request, 'form_generico.html', {
        'form': form, 'titulo': 'Cadastrar Serviço', 'cancel_url_name': 'servico_list'
    })


@login_required
def servico_update(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect('servico_list')
    else:
        form = ServicoForm(instance=servico)
    return render(request, 'form_generico.html', {
        'form': form, 'titulo': 'Editar Serviço', 'cancel_url_name': 'servico_list'
    })


@login_required
def servico_delete(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        servico.delete()
        return redirect('servico_list')
    return render(request, 'confirm_delete_generico.html', {
        'objeto': servico, 'cancel_url_name': 'servico_list', 'delete_url_name': 'servico_delete'
    })


# --- Pagamento ---
@login_required
def pagamento_list(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'pagamento_list.html', {'pagamentos': pagamentos})


@login_required
def pagamento_create(request):
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagamento_list')
    else:
        form = PagamentoForm()
    return render(request, 'form_generico.html', {
        'form': form, 'titulo': 'Cadastrar Pagamento', 'cancel_url_name': 'pagamento_list'
    })


@login_required
def pagamento_update(request, pk):
    pagamento = get_object_or_404(Pagamento, pk=pk)
    if request.method == 'POST':
        form = PagamentoForm(request.POST, instance=pagamento)
        if form.is_valid():
            form.save()
            return redirect('pagamento_list')
    else:
        form = PagamentoForm(instance=pagamento)
    return render(request, 'form_generico.html', {
        'form': form, 'titulo': 'Editar Pagamento', 'cancel_url_name': 'pagamento_list'
    })


@login_required
def pagamento_delete(request, pk):
    pagamento = get_object_or_404(Pagamento, pk=pk)
    if request.method == 'POST':
        pagamento.delete()
        return redirect('pagamento_list')
    return render(request, 'confirm_delete_generico.html', {
        'objeto': pagamento, 'cancel_url_name': 'pagamento_list', 'delete_url_name': 'pagamento_delete'
    })