from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('veiculos/', views.veiculo_list, name='veiculo_list'),
    path('veiculos/novo/', views.veiculo_create, name='veiculo_create'),
    path('veiculos/<int:pk>/editar/', views.veiculo_update, name='veiculo_update'),
    path('veiculos/<int:pk>/excluir/', views.veiculo_delete, name='veiculo_delete'),
    path('veiculos/consulta/', views.veiculo_consulta, name='veiculo_consulta'),

    path('os/', views.os_list, name='os_list'),
    path('os/nova/', views.os_create, name='os_create'),
    path('os/<int:pk>/editar/', views.os_update, name='os_update'),
    path('os/<int:pk>/excluir/', views.os_delete, name='os_delete'),

    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/novo/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/editar/', views.cliente_update, name='cliente_update'),
    path('clientes/<int:pk>/excluir/', views.cliente_delete, name='cliente_delete'),

    path('diagnosticos/', views.diagnostico_list, name='diagnostico_list'),
    path('diagnosticos/novo/', views.diagnostico_create, name='diagnostico_create'),
    path('diagnosticos/<int:pk>/editar/', views.diagnostico_update, name='diagnostico_update'),
    path('diagnosticos/<int:pk>/excluir/', views.diagnostico_delete, name='diagnostico_delete'),

    path('servicos/', views.servico_list, name='servico_list'),
    path('servicos/novo/', views.servico_create, name='servico_create'),
    path('servicos/<int:pk>/editar/', views.servico_update, name='servico_update'),
    path('servicos/<int:pk>/excluir/', views.servico_delete, name='servico_delete'),

    path('pagamentos/', views.pagamento_list, name='pagamento_list'),
    path('pagamentos/novo/', views.pagamento_create, name='pagamento_create'),
    path('pagamentos/<int:pk>/editar/', views.pagamento_update, name='pagamento_update'),
    path('pagamentos/<int:pk>/excluir/', views.pagamento_delete, name='pagamento_delete'),

]