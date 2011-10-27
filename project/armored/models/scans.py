from django.db import models
from core.models.scans import Scan

STATUS = [
    ("AGENDADO", "AGENDADO"),
    ("EXECUTANDO", "EXECUTANDO"),
    ("CONCLUIDO", "CONCLUIDO"),
    ("CANCELADO", "CANCELADO"),
    ("FALHOU", "FALHOU"),
    ("NA FILA", "NA FILA"),
]


class ArmoredScan(Scan):
    status = models.CharField(max_length=20, choices=STATUS)  # status
    percentage = models.PositiveIntegerField(default=0)  # percentual

    class Meta:
        abstract = True
        app_label = 'armored'
