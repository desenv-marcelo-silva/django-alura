# -*- coding: utf-8 -*-
from django.db import models

# usar python manage.py makemigrations para criar o esquema de migração (ver pasta migrate)

# usar python manage.py migrate para gerar o resultado deste migration no banco

# usar python manage.py shell para abrir um console onde pode-se instanciar e
# fazer operações como salvar dados nesta classe

#pode-se usar o comando python manage.py sqlmigrate [nome do app (aqui é perfis)] e o nome da migrate
#iso vai retornar os comandos SQL utilizados para rodar essa migração.

class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    empresa = models.CharField(max_length=255, null=False)