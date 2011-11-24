# -*- coding: utf-8 -*-

from django.db import models
# from devices import Device

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


class ScheduleType(models.Model):  # TipoScan
    name = models.CharField(max_length=50)  # nome
    description = models.CharField(max_length=200)  # descricao
    created_at = models.DateTimeField()  # created_at
    updated_at = models.DateTimeField()  # updated_at

    class Meta:
        app_label = 'core'


class Schedule(models.Model):  # Agendamentos
    device = models.ForeignKey("Device", null=True, blank=True, related_name="device_schedule")
    device_malware = models.ForeignKey("old.DispositivosMalware", null=True, blank=True, related_name="device_malware_schedule")
    schedule_start = models.DateTimeField()  # inicio_do_agendamento
    schedule_finish = models.DateTimeField()  # fim_do_agendamento
    scan_hour = models.TimeField()  # hora_do_scan
    frequency = models.CharField(max_length=20, choices=FREQUENCIA)  # frequencia
    active = models.BooleanField()  # ativo
    weekly_scan_day = models.PositiveIntegerField(choices=DAYS_OF_WEEK, null=True, blank=True)  # dia_scan_semanal
    monthly_scan_day = models.PositiveIntegerField(null=True, blank=True)  # dia_scan_mensal
    recurrent = models.BooleanField()  # recorrente
    schedule = models.ForeignKey(ScheduleType, null=True, blank=True)  # tipo_scan
    created_by = models.IntegerField(null=True, blank=True)  # usuario_id
    created_at = models.DateTimeField()  # created_at
    updated_at = models.DateTimeField()  # updated_at

    class Meta:
        app_label = 'core'
