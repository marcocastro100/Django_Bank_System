from django.db import models

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

    