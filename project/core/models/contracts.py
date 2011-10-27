from django.db import models
from clients import Client
from devices import Device


class Contract(models.Model):  # Contratos
    client = models.ForeignKey(Client)  # cliente_id
    start_date = models.DateField()  # data_inicio
    end_date = models.DateField()  # data_fim
    cancel_date = models.DateField(null=True, blank=True)  # data_recisao
    active = models.BooleanField()  # ativo
    trial = models.BooleanField()  # trial
    created_at = models.DateTimeField()  # created_at
    updated_at = models.DateTimeField()  # updated_at

    class Meta:
        app_label = 'core'


class Plan(models.Model):  # Planos
    name = models.CharField(max_length=150)  # nome
    description = models.TextField(blank=True)  # descricao
    frequency = models.CharField(max_length=100)  # periodicidade
    time_trial = models.PositiveIntegerField()  # tempo_trial
    seal = models.BooleanField()  # selo
    use_akamai = models.BooleanField()  # usa_akamai
    page_view_limit = models.BooleanField()  # limitar_page_views
    created_at = models.DateTimeField()  # created_at
    updated_at = models.DateTimeField()  # updated_at

    class Meta:
        app_label = 'core'


class PlanRange(models.Model):  # PlanoFaixas
    plan = models.ForeignKey(Plan)  # m_plano_id
    description = models.TextField(blank=True)  # descricao
    price = models.DecimalField(max_digits=10, decimal_places=2)  # valor
    price_anual = models.DecimalField(max_digits=10, decimal_places=2)  # valor_anual
    start_price = models.DecimalField(max_digits=10, decimal_places=2)  # taxa_ativacao
    dialy_page_views = models.PositiveIntegerField()  # page_views_diario
    monthly_page_views = models.PositiveIntegerField()  # page_views_mensal
    finance_code = models.IntegerField()  # sf_servico_cod
    created_at = models.DateTimeField()  # created_at
    updated_at = models.DateTimeField()  # updated_at

    class Meta:
        app_label = 'core'


class PlanContract(models.Model):  # Contrato Plano
    contract = models.ForeignKey(Contract)  # m_contrato_id
    plan = models.ForeignKey(Plan)  # m_plano_id
    plan_price = models.DecimalField(max_digits=10, decimal_places=2)  # valor_plano
    aditional_link_price = models.DecimalField(max_digits=10, decimal_places=2)  # valor_links_adicionais
    created_at = models.DateTimeField()  # created_at
    updated_at = models.DateTimeField()  # updated_at

    class Meta:
        app_label = 'core'
