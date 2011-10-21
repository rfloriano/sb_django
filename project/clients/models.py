# -*- coding: utf-8 -*-

from django.db import models

SCAN_PROVIDER_URL = [
    (1, "CENZIC"),
    (2, "QUALYS"),
    (3, "AVDS"),
]

SCAN_PROVIDER_IP = [
    (1, "AVDS"),
    (2, "QUALYS"),
]


class Client(models.Model):

    name = models.CharField(max_length=255)
    cep = models.CharField(max_length=9)
    address = models.CharField(max_length=255)
    complement = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=2)
    phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    cellphone = models.CharField(max_length=20)
    active = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    logo = models.ImageField(upload_to='clientes/logos')
    activation_code = models.CharField(max_length=100)
    activated_at = models.DateTimeField()
    nivel = models.PositiveIntegerField()
    scan_provider_url = models.PositiveIntegerField(choices=SCAN_PROVIDER_URL)
    scan_provider_ip = models.PositiveIntegerField(choices=SCAN_PROVIDER_IP)
    online = models.BooleanField()
    number = models.PositiveIntegerField()
    owner = models.BooleanField()
    cep_return = models.PositiveIntegerField()
    sid = models.CharField(max_length=100)
    vip_client = models.BooleanField()

    # class Meta():
    #     abstract = True

    # - id  int(11)
    # - type    varchar(255)
    # - nome    varchar(255)
    # - email   varchar(255)
    # - cep     varchar(255)
    # - endereco    text
    # - bairro  varchar(255)
    # - cidade  varchar(255)
    # - estado  varchar(255)
    # - telefone    varchar(255)
    # - fax     varchar(255)
    # - celular     varchar(255)
    # - ativo   tinyint(1)
    # - created_at  datetime
    # - updated_at  datetime
    # - activation_code     varchar(255)
    # - activated_at    datetime
    # - nivel   int(11)
    # - provedor_scan   int(11)
    # - provedor_scan_ip    int(11)
    # - online  tinyint(1)
    # - numero  int(11)
    # - complemento_endereco    varchar(255)
    # - proprietario    tinyint(1)
    # - tipo_retorno_por_cep    int(11)
    # - sid     varchar(16)
    # - vip_client  tinyint(1)


class Individual(Client):

    email = models.EmailField()
    cpf = models.PositiveIntegerField()
    rg = models.CharField(max_length=15)

    # cpf     varchar(255)
    # rg  varchar(255)


class LegalEntity(Client):

    cnpj = models.PositiveIntegerField()
    state_registration = models.CharField(max_length=100)
    name_representant = models.CharField(max_length=255)
    email_representant = models.EmailField()
    rg_representant = models.CharField(max_length=255)
    cpf_representant = models.PositiveIntegerField()

    # cnpj    varchar(255)
    # inscricao_estadual  varchar(255)
    # representante_nome  varchar(255)
    # representante_email     varchar(255)
    # representante_rg    varchar(255)
    # representante_cpf   varchar(255)


class Adquirente(Client):

    max_num_ips_pci = models.PositiveIntegerField()
