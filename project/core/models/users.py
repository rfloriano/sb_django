# # -*- coding: utf-8 -*-

# from django.db import models
# from clients import Acquirer


# class Users(models.Model):  # Usuarios
#     name = models.CharField(max_length=255)  # nome
#     crypted_password = models.CharField(max_length=120)
#     salt = models.CharField(max_length=120)
#     remember_token = models.CharField(max_length=120, blank=True)
#     remember_token_expires_at = models.DateTimeField(null=True, blank=True)
#     activation_code = models.CharField(max_length=120, blank=True)
#     activated_at = models.DateTimeField(null=True, blank=True)
#     login = models.CharField(max_length=300)
#     admin = models.BooleanField()
#     email = models.CharField(max_length=300)
#     reset_code = models.CharField(max_length=255)
#     accept = models.BooleanField(null=True)  # concordo
#     access_number = models.BooleanField(null=True)  # num_acessos
#     last_access = models.DateTimeField(null=True)  # ultimo_acesso
#     phone = models.CharField(max_length=765)  # telefone
#     cpf = models.CharField(max_length=765)  # cpf
#     accept_term_at = models.DateTimeField(null=True)  # termo_de_uso_aceito
#     failed_attempts = models.BooleanField(null=True)  # tentativas_falhas
#     last_attempts = models.DateTimeField(null=True)  # ultima_tentativa
#     # adquirente_id = models.IntegerField(null=True, blank=True)
#     owner = models.BooleanField()  # proprietario
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         app_label = 'core'


# class UserProfiles(models.Model):
#     user = models.ForeignKey(Users)  # usuario_id
#     stamp_enable_disable = models.BooleanField()
#     scan_finished = models.BooleanField()
#     vulnerability_critic_url = models.BooleanField()
#     vulnerability_critic_ip = models.BooleanField()
#     news_functions_information = models.BooleanField()
#     newsletter = models.BooleanField()
#     feed = models.BooleanField()
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     adquirente = models.ForeignKey(Acquirer, null=True, blank=True)

#     class Meta:
#         app_label = 'core'
