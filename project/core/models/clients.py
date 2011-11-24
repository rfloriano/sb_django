# # -*- coding: utf-8 -*-

# from django.db import models

# SCAN_PROVIDER_URL = [
#     (1, "CENZIC"),
#     (2, "QUALYS"),
#     (3, "AVDS"),
# ]

# SCAN_PROVIDER_IP = [
#     (1, "AVDS"),
#     (2, "QUALYS"),
# ]


# class Client(models.Model):  # Cliente
#     name = models.CharField(max_length=255)  # nome
#     cep = models.CharField(max_length=9)  # cep
#     address = models.CharField(max_length=255)  # endereco
#     complement = models.CharField(max_length=255, null=True, blank=True)   # complemento_endereco
#     neighborhood = models.CharField(max_length=255)  # bairro
#     city = models.CharField(max_length=100)  # cidade
#     province = models.CharField(max_length=2)  # estado
#     phone = models.CharField(max_length=20, null=True, blank=True)  # telefone
#     fax = models.CharField(max_length=20, null=True, blank=True)  # fax
#     cellphone = models.CharField(max_length=20, null=True, blank=True)  # celular
#     active = models.BooleanField()  # ativo
#     created_at = models.DateTimeField()  # created_at
#     updated_at = models.DateTimeField()  # updated_at
#     logo = models.ImageField(upload_to='clientes/logos')  # logo_file_name, logo_content_type, logo_file_size, logo_updated_at
#     activation_code = models.CharField(max_length=100)  # activation_code
#     activated_at = models.DateTimeField()  # activated_at
#     level = models.PositiveIntegerField()  # -- nivel
#     scan_provider_url = models.PositiveIntegerField(choices=SCAN_PROVIDER_URL)  # provedor_scan
#     scan_provider_ip = models.PositiveIntegerField(choices=SCAN_PROVIDER_IP)  # provedor_scan_ip
#     online = models.BooleanField()  # online
#     number = models.PositiveIntegerField()  # -- numero
#     owner = models.BooleanField()  # proprietario
#     cep_return = models.PositiveIntegerField()  # -- tipo_retorno_por_cep
#     sid = models.CharField(max_length=100)  # sid
#     vip_client = models.BooleanField()  # vip_client

#     class Meta:
#         app_label = 'core'


# class Individual(Client):  # PessoaFisica
#     email = models.EmailField()  # cliente.email
#     cpf = models.PositiveIntegerField()  # cliente.cpf
#     rg = models.CharField(max_length=15)  # cliente.rg

#     class Meta:
#         app_label = 'core'


# class LegalEntity(Client):  # PessoalJuridica
#     cnpj = models.PositiveIntegerField()  # cliente.cnpj
#     state_registration = models.CharField(max_length=100)  # cliente.inscricao_estadual
#     name_representant = models.CharField(max_length=255)  # cliente.representante_nome
#     email_representant = models.EmailField()  # cliente.representante_email
#     rg_representant = models.CharField(max_length=255)  # cliente.representante_rg
#     cpf_representant = models.PositiveIntegerField()  # cliente.representante_cpf

#     class Meta:
#         app_label = 'core'


# class Acquirer(Client):  # Adquirente
#     max_num_ips_pci = models.PositiveIntegerField()  # adquirente.max_num_ips_pci

#     class Meta:
#         app_label = 'core'
