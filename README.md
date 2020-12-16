# Django_Bank_System
Um sistema em django de um simples gerenciamento de transações bancarias (Sem FrontEnd elaborado...) desenvolvido para a disciplina de Topicos2 da UFVJM
Dupla: Marco Aurélio Rezende e Camila Aparecida Alves

O Sistema tem como função realizar o cadastramento das classes envolvidas em uma transação bancaria em uma base de dados e a partir destas realizar o gerenciamento de transações no sistema.

```python 
Modelo da base de dados:
class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.IntegerField()
    nascimento = models.IntegerField()
    def __str__(self):
        return(str(self.nome));

class Conta(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    numero = models.IntegerField()
    limite = models.IntegerField()
    saldo = models.IntegerField()
    def __str__(self):
        return(str(self.cliente)+'-'+str(self.numero));
        
class Transacao(models.Model):
    conta = models.ForeignKey(Conta,on_delete=models.CASCADE)
    tipo = models.CharField(choices=[('debito','debito'),('credito','credito')],max_length=50)
    valor = models.IntegerField()
```

Além de realizar o cadastro das categorias de Cliente, Conta e Transacao na base de dados, a aplicação visa o gerenciamento de transações que então atualizam os dados a ela relacionados na base de dados (saldo de conta por exemplo) e controlando as condições de transação como o saldo e limite bancarios da conta em questão, havendo também a opção de geração do extrato bancário associado à uma conta específica, que agrupará informações do cliente e contas envolvidas e todo o historico de transações da conta.

```python
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
```
