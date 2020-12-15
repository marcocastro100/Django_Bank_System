from django import forms 
from .models import Cliente,Conta,Transacao

class Clienteform(forms.ModelForm):
    class Meta:
        model = Cliente; #my model
        fields = "__all__"

class Contaform(forms.ModelForm):
    class Meta:
        model = Conta; #my model
        fields = "__all__"

class Transacaoform(forms.ModelForm):
    class Meta:
        model = Transacao; #my model
        fields = "__all__"

class Extractform(forms.ModelForm): #Just to show a form with client names to generate the extract
    class Meta:
        model = Transacao;
        fields = ('conta',); 