from django.urls import path, include #way to redirect web page to the project tree structure
from . import views

urlpatterns = [
    path('',views.main_list,name='list'),
    path('cliente_create/',views.cliente_create,name='cliente_create'),
    path('conta_create/',views.conta_create,name='conta_create'),
    path('transacao_create/',views.transacao_create,name='transacao_create'),
    path('extrato_create/',views.extrato_create,name='extrato_create'),
]