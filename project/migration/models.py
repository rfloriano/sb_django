from django.db import models
from old.models import PROVEDOR_SCAN, PROVEDOR_SCAN_IP


class Agendamentos(models.Model):
    id = models.IntegerField(primary_key=True)
    descricao = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    tipo = models.CharField(max_length=60, null=True, blank=True)
    frequencia = models.CharField(max_length=60, null=True, blank=True)
    inicio_do_agendamento = models.DateTimeField(null=True, blank=True)
    fim_do_agendamento = models.DateTimeField(null=True, blank=True)
    hora_do_scan = models.TimeField(null=True, blank=True)
    ativo = models.IntegerField(null=True, blank=True)
    data_criacao = models.DateTimeField(null=True, blank=True)
    usuario = models.ForeignKey("old.Usuarios", related_name="usuario_agendamentos", null=True, blank=True)
    client_id = models.CharField(max_length=45, blank=True)
    dispositivo = models.ForeignKey("Dispositivos", null=True, blank=True, related_name="device")
    status = models.CharField(max_length=90, null=True, blank=True)
    app_analysis = models.IntegerField(null=True, blank=True)
    tipo_scan = models.ForeignKey("TipoScans", null=True, blank=True, related_name="schedule_type")
    data_conclusao = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    provedor_utilizado = models.CharField(max_length=255, null=True, blank=True)
    dispositivo_malware = models.ForeignKey("old.DispositivosMalware", null=True, blank=True, related_name="device_malware")
    dia_scan_mensal = models.IntegerField(null=True, blank=True)
    recorrente = models.IntegerField(null=True, blank=True)
    dia_scan_semanal = models.IntegerField(null=True, blank=True)
    ultimo_scan_criado = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = u'agendamentos'

    def save(self):
        from core.models.schedules import Schedule

        if self.recorrente is None:
            self.recorrente = False

        Schedule.objects.get_or_create(
            id=self.id,
            device_id=self.dispositivo_id,
            device_malware_id=self.dispositivo_malware_id,
            schedule_start=self.inicio_do_agendamento,
            schedule_finish=self.fim_do_agendamento,
            scan_hour=self.hora_do_scan,
            frequency=self.frequencia,
            active=self.ativo,
            weekly_scan_day=self.dia_scan_semanal,
            monthly_scan_day=self.dia_scan_mensal,
            recurrent=self.recorrente,
            schedule_id=self.tipo_scan_id,
            created_by=self.usuario_id,
            created_at=self.created_at,
            updated_at=self.updated_at
        )


class Dispositivos(models.Model):
    nome = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True)
    cliente = models.ForeignKey("old.Clientes", null=True, blank=True, related_name="dispositivos_clientes")
    certificado = models.IntegerField(null=True, blank=True)
    ativo = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    acessos = models.IntegerField()
    ultima_certificacao = models.DateTimeField(null=True, blank=True)
    envia_email_vulnerabilidade = models.IntegerField(null=True, blank=True)
    aceite = models.IntegerField(null=True, blank=True)
    termo_de_uso = models.IntegerField(null=True, blank=True)
    aceite_cadastro = models.IntegerField(null=True, blank=True)
    selo_id = models.IntegerField(null=True, blank=True)
    primeira_certificacao = models.IntegerField(null=True, blank=True)
    num_vulns_1 = models.IntegerField(null=True, blank=True)
    num_vulns_2 = models.IntegerField(null=True, blank=True)
    num_vulns_3 = models.IntegerField(null=True, blank=True)
    num_vulns_4 = models.IntegerField(null=True, blank=True)
    num_vulns_5 = models.IntegerField(null=True, blank=True)
    alias = models.CharField(max_length=255, blank=True)
    idioma_selo = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    dispositivo_logo_file_name = models.CharField(max_length=255, blank=True)
    dispositivo_logo_content_type = models.CharField(max_length=255, blank=True)
    dispositivo_logo_file_size = models.IntegerField(null=True, blank=True)
    dispositivo_logo_updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = u'dispositivos'

    def save(self):
        from armored.models.devices import IpDevice, UrlDevice

        if self.num_vulns_1 is None:
            self.num_vulns_1 = 0

        if self.num_vulns_2 is None:
            self.num_vulns_2 = 0

        if self.num_vulns_3 is None:
            self.num_vulns_3 = 0

        if self.num_vulns_4 is None:
            self.num_vulns_4 = 0

        if self.num_vulns_5 is None:
            self.num_vulns_5 = 0

        if self.type == "Url":
            UrlDevice.objects.get_or_create(
                id=self.id,
                certified=self.certificado,
                description=self.description,
                number_access=self.acessos,
                logo_file_name=self.dispositivo_logo_file_name,
                logo_content_type=self.dispositivo_logo_content_type,
                logo_file_size=self.dispositivo_logo_file_size,
                logo_updated_at=self.dispositivo_logo_updated_at,
                object_type='UrlDevice',

                name=self.nome,
                client_id=self.cliente_id,
                active=self.ativo,
                accept=self.aceite,
                number_vulns_1=self.num_vulns_1,
                number_vulns_2=self.num_vulns_2,
                number_vulns_3=self.num_vulns_3,
                number_vulns_4=self.num_vulns_4,
                number_vulns_5=self.num_vulns_5,
                created_at=self.created_at,
                updated_at=self.updated_at,
            )
        elif self.type == "Ip":
            IpDevice.objects.get_or_create(
                id=self.id,
                alias=self.alias,
                object_type='IpDevice',

                name=self.nome,
                client_id=self.cliente_id,
                active=self.ativo,
                accept=self.aceite,
                number_vulns_1=self.num_vulns_1,
                number_vulns_2=self.num_vulns_2,
                number_vulns_3=self.num_vulns_3,
                number_vulns_4=self.num_vulns_4,
                number_vulns_5=self.num_vulns_5,
                created_at=self.created_at,
                updated_at=self.updated_at,
            )
        else:
            IpDevice.objects.get_or_create(
                id=self.id,
                alias=self.alias,
                object_type='IpPci',

                name=self.nome,
                client_id=self.cliente_id,
                active=self.ativo,
                accept=self.aceite,
                number_vulns_1=self.num_vulns_1,
                number_vulns_2=self.num_vulns_2,
                number_vulns_3=self.num_vulns_3,
                number_vulns_4=self.num_vulns_4,
                number_vulns_5=self.num_vulns_5,
                created_at=self.created_at,
                updated_at=self.updated_at,
            )


class TipoScans(models.Model):
    nome = models.CharField(max_length=150, blank=True)
    descricao = models.TextField(blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = u'tipo_scans'

    def save(self):
        from core.models.schedules import ScheduleType
        ScheduleType.objects.get_or_create(
            id=self.id,
            name=self.nome,
            description=self.descricao,
            created_at=self.created_at,
            updated_at=self.updated_at
        )


class Scans(models.Model):

    descricao = models.TextField(blank=True)
    data_do_scan = models.DateTimeField(null=True, blank=True)
    concluido = models.IntegerField(null=True, blank=True)
    data_criacao = models.DateTimeField(null=True, blank=True)
    agendamento = models.ForeignKey("Agendamentos", null=True, blank=True)
    request_id = models.CharField(unique=True, max_length=45, blank=True)
    status = models.CharField(max_length=90, blank=True)
    app_analysis = models.IntegerField(null=True, blank=True)
    data_conclusao = models.DateTimeField(null=True, blank=True)
    relatorio_cenzic = models.ForeignKey("RelatorioCenzics", null=True, blank=True)
    percentual = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    hackalert_id = models.IntegerField(null=True, blank=True)
    scan_avds_id = models.CharField(max_length=255, blank=True)
    webscan_avds_id = models.CharField(max_length=255, blank=True)
    error_description = models.CharField(max_length=255, blank=True)
    numero_tentativas = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'scans'

    def save(self):
        from armored.models.scans import AvdsScan, QualysScan
        from core.models.scans import Scan

        does_not_exist = []

        try:
            provedor_scan = dict(PROVEDOR_SCAN)[self.agendamento.dispositivo.cliente.provedor_scan]
            provedor_scan_ip = dict(PROVEDOR_SCAN_IP)[self.agendamento.dispositivo.cliente.provedor_scan_ip]

            if self.agendamento.provedor_utilizado is None:
                if self.agendamento.dispositivo.type == "Url":  # Default is cenzic
                    self.agendamento.provedor_utilizado = provedor_scan
                elif self.agendamento.dispositivo.type == "Ip":  # Default is avds
                    self.agendamento.provedor_utilizado = provedor_scan_ip
                elif self.agendamento.dispositivo.type == "IpPci":  # Default is qualys
                    self.agendamento.provedor_utilizado = "QUALYS"
                else:
                    does_not_exist.append("WARNING: Nothing to do with %s, type is not Url, Ip or IpPci\n" % self.id)

            if self.agendamento.provedor_utilizado == "CENZIC":
                Scan.objects.get_or_create(
                    id=self.id,
                    scan_type="OLD-CENZIC",

                    scan_date=self.data_do_scan,
                    schedule_id=self.agendamento_id,
                    scan_finished_date=self.data_conclusao,
                    error_description=self.error_description,
                    number_attempts=self.numero_tentativas,
                    status=self.status,
                    created_at=self.created_at,
                    updated_at=self.updated_at
                )
            elif self.agendamento.provedor_utilizado == "QUALYS":
                QualysScan.objects.get_or_create(
                    id=self.id,
                    scan_type="OLD-QUALYS",

                    scan_date=self.data_do_scan,
                    schedule_id=self.agendamento_id,
                    scan_finished_date=self.data_conclusao,
                    error_description=self.error_description,
                    number_attempts=self.numero_tentativas,
                    status=self.status,
                    created_at=self.created_at,
                    updated_at=self.updated_at
                )
            elif self.agendamento.provedor_utilizado == "AVDS":
                AvdsScan.objects.get_or_create(
                    id=self.id,
                    scan_type="AvdsScan",
                    scan_avds_id=self.scan_avds_id,
                    webscan_avds_id=self.webscan_avds_id,

                    scan_date=self.data_do_scan,
                    schedule_id=self.agendamento_id,
                    scan_finished_date=self.data_conclusao,
                    error_description=self.error_description,
                    number_attempts=self.numero_tentativas,
                    status=self.status,
                    created_at=self.created_at,
                    updated_at=self.updated_at
                )
            elif self.agendamento.provedor_utilizado == "Hack Alert - Malware":
                Scan.objects.get_or_create(
                    id=self.id,
                    scan_type="Hack Alert - Malware",
                    hackalert_id=self.hackalert_id,

                    scan_date=self.data_do_scan,
                    schedule_id=self.agendamento_id,
                    scan_finished_date=self.data_conclusao,
                    error_description=self.error_description,
                    number_attempts=self.numero_tentativas,
                    status=self.status,
                    created_at=self.created_at,
                    updated_at=self.updated_at
                )
            else:
                does_not_exist.append("WARNING: Nothing to do %s, provider is defined but not is Cenzic, Qualys, Avds or HackAlert\n", self.id)
        except Exception, e:
            does_not_exist.append("ERROR: %s to %s\n" % (e, self.id))

        f = file("scans.txt", "ab")
        f.writelines(does_not_exist)
        f.close()


class RelatorioCenzics(models.Model):
    duracao = models.IntegerField(null=True, blank=True)
    data_criacao = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    os = models.CharField(max_length=255, blank=True)
    nameserver = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'relatorio_cenzics'

    def save(self):
        pass
