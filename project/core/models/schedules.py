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
    ("IMEDIATAMENTE", "IMEDIATAMENTE"),
    ("DIARIAMENTE", "DIARIAMENTE"),
    ("SEMANALMENTE", "SEMANALMENTE"),
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
    recurrent = models.BooleanField()  # recorrente
    created_by = models.IntegerField(null=True, blank=True)  # usuario_id
    created_at = models.DateTimeField()  # created_at
    updated_at = models.DateTimeField()  # updated_at

    class Meta:
        app_label = 'core'
