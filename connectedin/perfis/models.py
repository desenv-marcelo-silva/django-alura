# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


# usar python manage.py makemigrations para criar o esquema de migração (ver pasta migrate)

# usar python manage.py migrate para gerar o resultado deste migration no banco

# usar python manage.py shell para abrir um console onde pode-se instanciar e
# fazer operações como salvar dados nesta classe

# pode-se usar o comando python manage.py sqlmigrate [nome do app (aqui é perfis)] e o nome da migrate
# iso vai retornar os comandos SQL utilizados para rodar essa migração.
# usando o shell também é possível criar diretamente um valor no banco para os models utilizando:
# perfil = Perfil.objects.create(nome='Steve', email='steve@minecraft.com', telefone='n/a', nome_empresa='Alura')

class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    #email = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    empresa = models.CharField(max_length=255, null=False)

    contatos = models.ManyToManyField('self')
    usuario = models.OneToOneField(User, related_name='perfil')

    @property
    def email(self):
        return self.usuario.email

    def convidar(self, perfil_convidado):
        convite = Convite(solicitante=self, convidado=perfil_convidado).save()

class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, related_name='convites_feitos')
    convidado = models.ForeignKey(Perfil, related_name='convites_recebidos')

    def aceitar(self):
        self.convidado.contatos.add(self.solicitante)
        self.solicitante.contatos.add(self.convidado)
        self.delete()