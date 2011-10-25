# -*- coding: utf-8 -*-

from django.db import models

DAYS_OF_WEEK = (
    (0, 'Domingo'),
    (1, 'Segunda-feira'),
    (2, 'Terça-feira'),
    (3, 'Quarta-feira'),
    (4, 'Quinta-feira'),
    (5, 'Sexta-feira'),
    (6, 'Sábado'),
)

FREQUENCIA = [
    ("IMEDIATAMENTE" "IMEDIATAMENTE"),
    ("DIARIAMENTE" "DIARIAMENTE"),
    ("SEMANALMENTE" "SEMANALMENTE"),
    ("MENSALMENTE", "MENSALMENTE"),
]


class Schedule(models.Model):  # Agendamentos
    schedule_start = models.DateTimeField()  # inicio_do_agendamento
    schedule_finish = models.DateTimeField()  # fim_do_agendamento
    scan_hour = models.TimeField()  # hora_do_scan
    frequency = models.CharField(max_length=20, choices=FREQUENCIA)  # frequencia
    active = models.BooleanField()  # ativo
    weekly_scan_day = models.PositiveIntegerField(choices=DAYS_OF_WEEK, null=True, blank=True)  # dia_scan_semanal
    monthly_scan_day = models.PositiveIntegerField(null=True, blank=True)  # dia_scan_mensal
    recorrente = models.IntegerField(null=True, blank=True)
    usuario_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        app_label = 'blindado'

    # descricao = models.CharField(max_length=300, blank=True)
    # url = models.CharField(max_length=300, blank=True)

    # status = models.CharField(max_length=90, blank=True)
    # app_analysis = models.IntegerField(null=True, blank=True)
    # data_conclusao = models.DateTimeField(null=True, blank=True)
    # ultimo_scan_criado = models.DateTimeField(null=True, blank=True)

    # tipo = models.CharField(max_length=60, blank=True)

    # client_id = models.CharField(max_length=45, blank=True)
    # provedor_utilizado = models.CharField(max_length=765, blank=True)

    # dispositivo_id = models.IntegerField(null=True, blank=True)
    # dispositivo_malware_id = models.IntegerField(null=True, blank=True)

    tipo_scan_id = models.IntegerField(null=True, blank=True)