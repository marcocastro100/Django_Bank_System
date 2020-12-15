from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Cliente,Conta,Transacao
from .forms import Clienteform,Contaform,Transacaoform,Extractform

def main_list(request):
    clientes = Cliente.objects.all();
    contas = Conta.objects.all();
    transactions = Transacao.objects.all();
    return(render(request,'bank/templates/list.html',{'clientes':clientes,'contas':contas,'transactions':transactions}))

def cliente_create(request):
    form = Clienteform;
    if(request.method == 'POST'):
        filled_form = Clienteform(request.POST);
        filled_form.save()
        return(redirect('/'))
    return(render(request,'bank/templates/Create_cliente.html',{'form':form}))

def conta_create(request):
    form = Contaform;
    if(request.method == 'POST'):
        filled_form = Contaform(request.POST);
        filled_form.save()
        return(redirect('/'))
    return(render(request,'bank/templates/Create_conta.html',{'form':form}))

def transacao_create(request):
    form = Transacaoform;
    if(request.method == 'POST'):
            #Retrieve information on post request
        instance_conta = Conta.objects.get(id=request.POST['conta'])
        instance_tipo = request.POST['tipo'];
        instance_valor = int(request.POST['valor']);
            #Check if valid
        filled_form = Transacaoform(request.POST);
        if(instance_tipo == 'debito'):
            if(instance_valor <= instance_conta.saldo):
                filled_form.save(); #Salva registro de transação
                instance_conta.saldo -= instance_valor; #Altera saldo da conta
                instance_conta.save() #Salva alteração do saldo da conta
            else: return(HttpResponse('<h5>Impossível com o saldo de conta atual!</h5>'))
        elif(instance_tipo == 'credito'):
            if((instance_valor+instance_conta.saldo) <= instance_conta.limite):
                filled_form.save();
                instance_conta.saldo += instance_valor;
                instance_conta.save()
            else: return(HttpResponse('<h5>Impossível com o limite de conta atual!</h5>'))
        return(redirect('/'))
    return(render(request,'bank/templates/Create_transacao.html',{'form':form}))

def extrato_create(request):
    form = Extractform;
    if(request.method == 'POST'):
        conta = Conta.objects.get(id=request.POST['conta']);
        cliente = Cliente.objects.get(id = conta.cliente.id);
        transacoes = Transacao.objects.filter(conta = conta);
        return (render(request,'bank/templates/Create_extrato.html',{
            'conta':conta,
            'cliente':cliente,
            'transacoes':transacoes
        }))
    return(render(request,'bank/templates/Create_extrato.html',{'form':form}))

