# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Adquirentes(models.Model):
    
    nome = models.CharField(unique=True, max_length=255, blank=True)
    logo = models.CharField(max_length=255, blank=True)
    cliente = models.ForeignKey("Clientes")
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    max_num_ips_pci = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'adquirentes'

class Agendamentos(models.Model):
    
    descricao = models.TextField(blank=True)
    url = models.CharField(max_length=255, blank=True)
    tipo = models.CharField(max_length=60, blank=True)
    frequencia = models.CharField(max_length=60, blank=True)
    inicio_do_agendamento = models.DateTimeField(null=True, blank=True)
    fim_do_agendamento = models.DateTimeField(null=True, blank=True)
    hora_do_scan = models.TimeField(blank=True) # This field type is a guess.
    ativo = models.IntegerField(null=True, blank=True)
    data_criacao = models.DateTimeField(null=True, blank=True)
    usuario = models.ForeignKey("Usuarios", null=True, blank=True, related_name="user_schedule")
    client_id = models.CharField(max_length=45, blank=True)
    dispositivo = models.ForeignKey("core.Device", null=True, blank=True, related_name="device")
    status = models.CharField(max_length=90, blank=True)
    app_analysis = models.IntegerField(null=True, blank=True)
    tipo_scan = models.ForeignKey("core.ScheduleType", null=True, blank=True, related_name="schedule_type")
    data_conclusao = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    provedor_utilizado = models.CharField(max_length=255, blank=True)
    dispositivo_malware = models.ForeignKey("DispositivosMalware", null=True, blank=True, related_name="device_malware")
    dia_scan_mensal = models.IntegerField(null=True, blank=True)
    recorrente = models.IntegerField(null=True, blank=True)
    dia_scan_semanal = models.IntegerField(null=True, blank=True)
    ultimo_scan_criado = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'agendamentos'

class Assinaturas(models.Model):
    
    cliente = models.ForeignKey("Clientes", related_name="client_signature")
    plano = models.ForeignKey("Planos", related_name="plan")
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    ativa = models.IntegerField(null=True, blank=True)
    data_rescisao = models.DateField(null=True, blank=True)
    type = models.CharField(max_length=255, blank=True)
    assinatura_base = models.ForeignKey("Assinaturas", null=True, blank=True, related_name="sign")
    quantidade = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'assinaturas'

# class AtaqueItens(models.Model):
    
#     ataque_id = models.IntegerField(null=True, blank=True)
#     tipo = models.CharField(max_length=150, blank=True)
#     severidade = models.CharField(max_length=150, blank=True)
#     url = models.CharField(max_length=255, blank=True)
#     mensagem = models.TextField(blank=True)
#     data_criacao = models.DateTimeField(null=True, blank=True)
#     created_at = models.DateTimeField(null=True, blank=True)
#     updated_at = models.DateTimeField(null=True, blank=True)
#     http_request = models.TextField(blank=True)
#     http_response = models.TextField(blank=True)
#     class Meta:
#         db_table = u'ataque_itens'

# class Ataques(models.Model):
    
#     relatorio_cenzic_id = models.IntegerField(null=True, blank=True)
#     nome = models.CharField(max_length=255, blank=True)
#     descricao = models.TextField(blank=True)
#     como_funciona = models.TextField(blank=True)
#     impacto = models.TextField(blank=True)
#     solucao = models.TextField(blank=True)
#     nivel = models.IntegerField(null=True, blank=True)
#     tipo = models.TextField(blank=True)
#     created_at = models.DateTimeField(null=True, blank=True)
#     updated_at = models.DateTimeField(null=True, blank=True)
#     test_id = models.IntegerField(null=True, blank=True)
#     reference = models.TextField(blank=True)
#     avds_vulnerabilidade_id = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'ataques'

# class AvdsVulnerabilidades(models.Model):
    
#     family = models.TextField(blank=True)
#     name = models.TextField(blank=True)
#     description = models.TextField(blank=True)
#     how_it_works = models.TextField(blank=True)
#     impact = models.TextField(blank=True)
#     solution = models.TextField(blank=True)
#     risk = models.IntegerField(null=True, blank=True)
#     test_id = models.IntegerField(null=True, blank=True)
#     service = models.CharField(max_length=255, blank=True)
#     class Meta:
#         db_table = u'avds_vulnerabilidades'

class Blacklists(models.Model):
    
    url = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'blacklists'

class ClientNotifications(models.Model):
    
    title = models.CharField(max_length=255, blank=True)
    preview = models.TextField(blank=True)
    link = models.CharField(max_length=255, blank=True)
    publication = models.DateField(null=True, blank=True)
    cliente = models.ForeignKey("Clientes", null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'client_notifications'

class Clientes(models.Model):
    
    type = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255, blank=True)
    cnpj = models.CharField(max_length=255, blank=True)
    inscricao_estadual = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    cep = models.CharField(max_length=255, blank=True)
    endereco = models.TextField(blank=True)
    bairro = models.CharField(max_length=255, blank=True)
    cidade = models.CharField(max_length=255, blank=True)
    estado = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255, blank=True)
    fax = models.CharField(max_length=255, blank=True)
    celular = models.CharField(max_length=255, blank=True)
    ativo = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    rg = models.CharField(max_length=255, blank=True)
    descricao = models.TextField(blank=True)
    observacoes = models.TextField(blank=True)
    url = models.CharField(max_length=255, blank=True)
    segmento = models.IntegerField(null=True, blank=True)
    logo_file_name = models.CharField(max_length=255, blank=True)
    logo_content_type = models.CharField(max_length=255, blank=True)
    logo_file_size = models.IntegerField(null=True, blank=True)
    logo_updated_at = models.DateTimeField(null=True, blank=True)
    representante_nome = models.CharField(max_length=255, blank=True)
    representante_email = models.CharField(max_length=255, blank=True)
    representante_rg = models.CharField(max_length=255, blank=True)
    representante_cpf = models.CharField(max_length=255, blank=True)
    activation_code = models.CharField(max_length=255, blank=True)
    activated_at = models.DateTimeField(null=True, blank=True)
    tipo_questionario = models.CharField(max_length=255, blank=True)
    nivel = models.IntegerField(null=True, blank=True)
    provedor_scan = models.IntegerField(null=True, blank=True)
    provedor_scan_ip = models.IntegerField(null=True, blank=True)
    online = models.IntegerField(null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    complemento_endereco = models.CharField(max_length=255, blank=True)
    proprietario = models.IntegerField(null=True, blank=True)
    tipo_retorno_por_cep = models.IntegerField(null=True, blank=True)
    sid = models.CharField(max_length=48, blank=True)
    vip_client = models.IntegerField(null=True, blank=True)
    parceiro_dono = models.IntegerField(null=True, blank=True)
    is_parceiro = models.IntegerField(null=True, blank=True)
    parceiro = models.ForeignKey("Parceiros", null=True, blank=True)
    class Meta:
        db_table = u'clientes'

class ClientesGrupos(models.Model):
    cliente = models.ForeignKey("Clientes", null=True, blank=True, related_name="client_groups")
    grupo = models.ForeignKey("Grupos", null=True, blank=True, related_name="group")
    class Meta:
        db_table = u'clientes_grupos'

class Configuracoes(models.Model):
    nome = models.CharField(max_length=255, blank=True)
    descricao = models.CharField(max_length=255, blank=True)
    frequencia = models.IntegerField(null=True, blank=True)
    timeout = models.IntegerField(null=True, blank=True)
    nr_max_scans = models.IntegerField(null=True, blank=True)
    param1 = models.CharField(max_length=255, blank=True)
    param2 = models.CharField(max_length=255, blank=True)
    param3 = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'configuracoes'

class Consultas(models.Model):
    
    ip_requisicao = models.CharField(max_length=255, blank=True)
    nome = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    dominio = models.CharField(max_length=255, blank=True)
    blindado = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'consultas'

class Contratos(models.Model):
    
    cliente = models.ForeignKey("Clientes", null=True, blank=True, related_name="client_contract")
    m_plano = models.ForeignKey("MPlanos", null=True, blank=True, related_name="plan_malware")
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    ativo = models.IntegerField(null=True, blank=True)
    data_rescisao = models.DateField(null=True, blank=True)
    tipo = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'contratos'

# class DashboardDeviceAndVulrenabilitys(models.Model):
    
#     device_id = models.CharField(max_length=255, blank=True)
#     created_at = models.DateTimeField(null=True, blank=True)
#     updated_at = models.DateTimeField(null=True, blank=True)
#     object_type = models.CharField(max_length=255, blank=True)
#     object_id = models.IntegerField(null=True, blank=True)
#     object_data = models.CharField(max_length=255, blank=True)
#     class Meta:
#         db_table = u'dashboard_device_and_vulrenabilitys'

# class DashboardStats(models.Model):
    
#     created_at = models.DateTimeField(null=True, blank=True)
#     updated_at = models.DateTimeField(null=True, blank=True)
#     nivel_1 = models.IntegerField(null=True, blank=True)
#     nivel_2 = models.IntegerField(null=True, blank=True)
#     nivel_3 = models.IntegerField(null=True, blank=True)
#     nivel_4 = models.IntegerField(null=True, blank=True)
#     nivel_5 = models.IntegerField(null=True, blank=True)
#     cliente_id = models.IntegerField(null=True, blank=True)
#     report_date = models.DateTimeField(null=True, blank=True)
#     class Meta:
#         db_table = u'dashboard_stats'

# class DashboardTops(models.Model):
    
#     quantity = models.IntegerField(null=True, blank=True)
#     created_at = models.DateTimeField(null=True, blank=True)
#     updated_at = models.DateTimeField(null=True, blank=True)
#     object_type = models.CharField(max_length=255, blank=True)
#     object_id = models.IntegerField(null=True, blank=True)
#     object_data = models.CharField(max_length=255, blank=True)
#     class Meta:
#         db_table = u'dashboard_tops'

# class Dispositivos(models.Model):
    
#     nome = models.CharField(max_length=255, blank=True)
#     type = models.CharField(max_length=255, blank=True)
#     cliente_id = models.IntegerField(null=True, blank=True)
#     certificado = models.IntegerField(null=True, blank=True)
#     ativo = models.IntegerField(null=True, blank=True)
#     created_at = models.DateTimeField(null=True, blank=True)
#     updated_at = models.DateTimeField(null=True, blank=True)
#     acessos = models.IntegerField()
#     ultima_certificacao = models.DateTimeField(null=True, blank=True)
#     envia_email_vulnerabilidade = models.IntegerField(null=True, blank=True)
#     aceite = models.IntegerField(null=True, blank=True)
#     termo_de_uso = models.IntegerField(null=True, blank=True)
#     aceite_cadastro = models.IntegerField(null=True, blank=True)
#     selo_id = models.IntegerField(null=True, blank=True)
#     primeira_certificacao = models.IntegerField(null=True, blank=True)
#     num_vulns_1 = models.IntegerField(null=True, blank=True)
#     num_vulns_2 = models.IntegerField(null=True, blank=True)
#     num_vulns_3 = models.IntegerField(null=True, blank=True)
#     num_vulns_4 = models.IntegerField(null=True, blank=True)
#     num_vulns_5 = models.IntegerField(null=True, blank=True)
#     alias = models.CharField(max_length=255, blank=True)
#     idioma_selo = models.CharField(max_length=255, blank=True)
#     description = models.TextField(blank=True)
#     dispositivo_logo_file_name = models.CharField(max_length=255, blank=True)
#     dispositivo_logo_content_type = models.CharField(max_length=255, blank=True)
#     dispositivo_logo_file_size = models.IntegerField(null=True, blank=True)
#     dispositivo_logo_updated_at = models.DateTimeField(null=True, blank=True)
#     class Meta:
#         db_table = u'dispositivos'

class DispositivosMalware(models.Model):
    
    nome = models.CharField(max_length=255, blank=True)
    alias = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True)
    cliente = models.ForeignKey("Clientes", null=True, blank=True)
    certificado = models.IntegerField(null=True, blank=True)
    ativo = models.IntegerField(null=True, blank=True)
    quantidade_links = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    quantidade_links_adicionais = models.IntegerField(null=True, blank=True)
    selo_id = models.IntegerField(null=True, blank=True)
    removido = models.IntegerField(null=True, blank=True)
    trial_bloqueado = models.IntegerField(null=True, blank=True)
    liberar_selo = models.IntegerField()
    class Meta:
        db_table = u'dispositivos_malware'

class EstatisticaContas(models.Model):
    
    clientes_count = models.IntegerField(null=True, blank=True)
    contas_ativas_count = models.IntegerField(null=True, blank=True)
    ips_disponiveis = models.IntegerField(null=True, blank=True)
    ips_cadastrados = models.IntegerField(null=True, blank=True)
    scans_realizados = models.IntegerField(null=True, blank=True)
    adquirente = models.ForeignKey("Adquirentes", null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    max_num_ips_pci = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'estatistica_contas'

class Estatisticas(models.Model):
    page_views = models.IntegerField(null=True, blank=True)
    banda = models.IntegerField(null=True, blank=True)
    dispositivo = models.ForeignKey("core.Device", null=True, blank=True)
    mes_ano = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    page_views_akamai = models.IntegerField(null=True, blank=True)
    banda_akamai = models.IntegerField(null=True, blank=True)
    dispositivo_malware_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'estatisticas'

class FeedReports(models.Model):
    
    feed = models.ForeignKey("Feeds", null=True, blank=True)
    _report_id = models.IntegerField(null=True, blank=True)
    _report_type = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'feed_reports'

class Feeds(models.Model):
    
    usuario = models.ForeignKey("Usuarios", null=True, blank=True)
    private_key = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'feeds'

class Grupos(models.Model):
    
    nome = models.CharField(max_length=255, blank=True)
    adquirente = models.ForeignKey("Adquirentes", null=True, blank=True)
    quinzenas = models.CharField(max_length=255, blank=True)
    ativo = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'grupos'

class HaProfilingReports(models.Model):
    
    data = models.TextField(blank=True)
    scan_status = models.ForeignKey("HaScanStatus", null=True, blank=True)
    class Meta:
        db_table = u'ha_profiling_reports'

class HaScanStatus(models.Model):
    
    scan_request_id = models.IntegerField(null=True, blank=True)
    scan_result_id = models.IntegerField(null=True, blank=True)
    scan_request_hostname = models.CharField(max_length=255, blank=True)
    scan_started_at = models.DateTimeField(null=True, blank=True)
    scan_completed_at = models.DateTimeField(null=True, blank=True)
    scan_hostname = models.CharField(max_length=255, blank=True)
    entrypoint = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255, blank=True)
    failure_code = models.CharField(max_length=255, blank=True)
    failure_reason = models.CharField(max_length=255, blank=True)
    internal_pages_scanned = models.IntegerField(null=True, blank=True)
    external_pages_scanned = models.IntegerField(null=True, blank=True)
    http_pages_scanned = models.IntegerField(null=True, blank=True)
    https_pages_scanned = models.IntegerField(null=True, blank=True)
    scan_time = models.IntegerField(null=True, blank=True)
    estimated_time_of_completion = models.DateTimeField(null=True, blank=True)
    position_in_queue = models.IntegerField(null=True, blank=True)
    scan = models.ForeignKey("core.Scan", null=True, blank=True)
    class Meta:
        db_table = u'ha_scan_status'

class HaScannedUrls(models.Model):
    
    url = models.CharField(max_length=255, blank=True)
    blacklisted_data = models.TextField(blank=True)
    malicious_data = models.TextField(blank=True)
    suspicious_data = models.TextField(blank=True)
    scan_status = models.ForeignKey("HaScanStatus", null=True, blank=True)
    class Meta:
        db_table = u'ha_scanned_urls'

class LogonImages(models.Model):
    
    caption = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    picture_file_name = models.CharField(max_length=255, blank=True)
    picture_content_type = models.CharField(max_length=255, blank=True)
    picture_file_size = models.IntegerField(null=True, blank=True)
    picture_updated_at = models.DateTimeField(null=True, blank=True)
    link = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'logon_images'

class Logs(models.Model):
    
    erro = models.TextField(blank=True)
    mensagem = models.TextField(blank=True)
    trace = models.TextField(blank=True)
    scan = models.ForeignKey("core.Scan", null=True, blank=True)
    data_criacao = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'logs'

class MContratos(models.Model):
    
    cliente = models.ForeignKey("Clientes", null=True, blank=True)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    ativo = models.IntegerField(null=True, blank=True)
    data_rescisao = models.DateField(null=True, blank=True)
    tipo = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    trial = models.IntegerField(null=True, blank=True)
    sf_contrato_cod = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'm_contratos'

class MContratosPlanos(models.Model):
    
    m_contrato = models.ForeignKey("MContratos")
    m_plano_id = models.IntegerField("MPlanos")
    dispositivo_malware_id = models.IntegerField()
    valor_plano = models.DecimalField(max_digits=10, decimal_places=2)
    valor_links_adicionais = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'm_contratos_planos'

class MPlanoFaixas(models.Model):
    
    m_plano = models.ForeignKey("MPlanos")
    quantidade_links = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    sf_servico_cod = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'm_plano_faixas'

class MPlanos(models.Model):
    
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    num_urls = models.IntegerField()
    periodicidade = models.CharField(max_length=255)
    tempo_trial = models.IntegerField()
    selo = models.IntegerField()
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    plano_site_blindado_flag = models.IntegerField(null=True, blank=True)
    gratuito = models.IntegerField(null=True, blank=True)
    page_views_mensal = models.IntegerField(null=True, blank=True)
    limitar_page_views = models.IntegerField()
    nivel_alerta_page_views = models.IntegerField()
    class Meta:
        db_table = u'm_planos'

class Movimentacoes(models.Model):
    
    usuario = models.ForeignKey("Usuarios", related_name="user_movimentation")
    acao = models.CharField(max_length=255)
    dispositivo = models.CharField(max_length=255, blank=True)
    justificativa = models.TextField(blank=True)
    cliente = models.ForeignKey("Clientes", null=True, blank=True, related_name="client_movimentation")
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'movimentacoes'

class Notifications(models.Model):
    
    title = models.CharField(max_length=255, blank=True)
    preview = models.TextField(blank=True)
    link = models.CharField(max_length=255, blank=True)
    publication = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'notifications'

class Parceiros(models.Model):
    
    codigo = models.CharField(max_length=255, blank=True)
    url_selo = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'parceiros'

class Perguntas(models.Model):
    
    texto = models.TextField(blank=True)
    requisito = models.ForeignKey("Requisitos", null=True, blank=True, related_name="requisito")
    questionario = models.ForeignKey("Questionarios", null=True, blank=True, related_name="questinnaire")
    dica = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    titulo = models.IntegerField(null=True, blank=True)
    pergunta_mae_id = models.IntegerField(null=True, blank=True)
    numero = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'perguntas'

class Permissoes(models.Model):
    
    usuario = models.ForeignKey("Usuarios", related_name="user_permission")
    cliente = models.ForeignKey("Clientes", null=True, blank=True, related_name="client_permission")
    papel = models.IntegerField()
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'permissoes'

class Pesquisas(models.Model):
    
    data_inicio = models.DateTimeField(null=True, blank=True)
    data_fim = models.DateTimeField(null=True, blank=True)
    dispositivo = models.ForeignKey("core.Device", null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    vendas_desde_ultimo_email = models.IntegerField(null=True, blank=True)
    ultimo_email_enviado = models.DateTimeField(null=True, blank=True)
    envia_email_finalizado = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=255, blank=True)
    codigo_promocional = models.CharField(max_length=765, blank=True)
    resultado_pesquisa_menor_id = models.IntegerField("ResultadoPesquisas", null=True, blank=True)
    class Meta:
        db_table = u'pesquisas'

class Planos(models.Model):
    
    nome = models.CharField(max_length=255)
    valor_mensal = models.FloatField()
    num_ips = models.IntegerField()
    num_urls = models.IntegerField()
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    page_views_diario = models.IntegerField(null=True, blank=True)
    descricao = models.TextField(blank=True)
    valor_anual = models.FloatField()
    taxa_ativacao = models.FloatField()
    page_views_mensal = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=255, blank=True)
    usa_selo_akamai = models.IntegerField(null=True, blank=True)
    num_ips_pci = models.IntegerField(null=True, blank=True)
    plano_site_blindado = models.TextField(blank=True) # This field type is a guess.
    plano_malware = models.ForeignKey("MPlanos", null=True, blank=True)
    class Meta:
        db_table = u'planos'

class QuestionarioClientes(models.Model):
    
    questionario = models.ForeignKey("Questionarios", null=True, blank=True, related_name="questionnaire")
    cliente = models.ForeignKey("Clientes", null=True, blank=True, related_name="client_questionnaire")
    respostas_count = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    nome = models.CharField(max_length=255, blank=True)
    dbas = models.CharField(max_length=255, blank=True)
    contato = models.CharField(max_length=255, blank=True)
    tipos_negocio = models.TextField(blank=True)
    relacionamento_prestadores_servico = models.IntegerField(null=True, blank=True)
    relacionamento_adquirente = models.IntegerField(null=True, blank=True)
    aplicativo_pagamento = models.CharField(max_length=255, blank=True)
    versao_aplicativo_pagamento = models.CharField(max_length=255, blank=True)
    questionario_preenchido = models.IntegerField(null=True, blank=True)
    informacoes_representam_resultados = models.IntegerField(null=True, blank=True)
    confirmacao_nao_armazenamento_dados_autenticacao = models.IntegerField(null=True, blank=True)
    reconhecimento_conformidade_total = models.IntegerField(null=True, blank=True)
    sem_evidencias_armazenamento_dados = models.IntegerField(null=True, blank=True)
    responsavel_executivo = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'questionario_clientes'

class Questionarios(models.Model):
    
    nome = models.CharField(max_length=255, blank=True)
    ativo = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'questionarios'

# class Referencias(models.Model):
    
#     vulnerabilidade_id = models.IntegerField(null=True, blank=True)
#     tipo = models.CharField(max_length=255, blank=True)
#     url = models.CharField(max_length=255, blank=True)
#     rid = models.CharField(max_length=255, blank=True)
#     description = models.TextField(blank=True)
#     section = models.CharField(max_length=255, blank=True)
#     compliance_type = models.CharField(max_length=255, blank=True)
#     info = models.CharField(max_length=255, blank=True)
#     created_at = models.DateTimeField(null=True, blank=True)
#     updated_at = models.DateTimeField(null=True, blank=True)
#     class Meta:
#         db_table = u'referencias'

# class RelatorioCenzics(models.Model):
    
#     duracao = models.IntegerField(null=True, blank=True)
#     data_criacao = models.DateTimeField(null=True, blank=True)
#     created_at = models.DateTimeField(null=True, blank=True)
#     updated_at = models.DateTimeField(null=True, blank=True)
#     os = models.CharField(max_length=255, blank=True)
#     nameserver = models.CharField(max_length=255, blank=True)
#     class Meta:
#         db_table = u'relatorio_cenzics'

# class RelatorioVulnerabilidades(models.Model):
    
#     relatorio_id = models.IntegerField(null=True, blank=True)
#     vulnerabilidade_id = models.IntegerField(null=True, blank=True)
#     result = models.TextField(blank=True)
#     tipo = models.CharField(max_length=255, blank=True)
#     created_at = models.DateTimeField(null=True, blank=True)
#     updated_at = models.DateTimeField(null=True, blank=True)
#     format_table = models.IntegerField(null=True, blank=True)
#     port = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'relatorio_vulnerabilidades'

# class Relatorios(models.Model):
    
#     scan_ref = models.CharField(max_length=255, blank=True)
#     username = models.CharField(max_length=255, blank=True)
#     company = models.CharField(max_length=255, blank=True)
#     date = models.DateTimeField(null=True, blank=True)
#     title = models.CharField(max_length=255, blank=True)
#     target = models.CharField(max_length=255, blank=True)
#     duration = models.CharField(max_length=255, blank=True)
#     scan_host = models.CharField(max_length=255, blank=True)
#     nbhost_alive = models.IntegerField(null=True, blank=True)
#     nbhost_total = models.IntegerField(null=True, blank=True)
#     report_type = models.CharField(max_length=255, blank=True)
#     options = models.TextField(blank=True)
#     status = models.CharField(max_length=255, blank=True)
#     asset_group = models.CharField(max_length=255, blank=True)
#     option_profile = models.CharField(max_length=255, blank=True)
#     ip = models.CharField(max_length=255, blank=True)
#     nameserver = models.CharField(max_length=255, blank=True)
#     os = models.CharField(max_length=255, blank=True)
#     created_at = models.DateTimeField(null=True, blank=True)
#     updated_at = models.DateTimeField(null=True, blank=True)
#     atualizado = models.IntegerField(null=True, blank=True)
#     dispositivo_id = models.IntegerField(null=True, blank=True)
#     cliente_id = models.IntegerField(null=True, blank=True)
#     scan_manual = models.IntegerField(null=True, blank=True)
#     type = models.CharField(max_length=255, blank=True)
#     merchant_name = models.CharField(max_length=255, blank=True)
#     num_hosts_compliant = models.IntegerField(null=True, blank=True)
#     compliance_status = models.CharField(max_length=255, blank=True)
#     partner_name = models.CharField(max_length=255, blank=True)
#     scan_module = models.CharField(max_length=255, blank=True)
#     port = models.IntegerField(null=True, blank=True)
#     qualys_id_relatorio = models.CharField(max_length=255, blank=True)
#     class Meta:
#         db_table = u'relatorios'

class Requisitos(models.Model):
    
    numero = models.IntegerField(null=True, blank=True)
    descricao = models.TextField(blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'requisitos'

class Respostas(models.Model):
    
    pergunta = models.ForeignKey("Perguntas", null=True, blank=True, related_name="question")
    opcao = models.IntegerField(null=True, blank=True)
    comentario = models.TextField(blank=True)
    questionario_cliente = models.ForeignKey("QuestionarioClientes", null=True, blank=True, related_name="questionnaire")
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'respostas'

class ResultadoPesquisas(models.Model):
    
    viu_selo = models.IntegerField(null=True, blank=True)
    data_compra = models.DateTimeField(null=True, blank=True)
    compras_duplicadas = models.IntegerField(null=True, blank=True)
    ip = models.CharField(max_length=255, blank=True)
    url_compra = models.CharField(max_length=255, blank=True)
    pesquisa = models.ForeignKey("Pesquisas", null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    comprou = models.IntegerField(null=True, blank=True)
    preco = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'resultado_pesquisas'

# class Scans(models.Model):
    
#     descricao = models.TextField(blank=True)
#     data_do_scan = models.DateTimeField(null=True, blank=True)
#     concluido = models.IntegerField(null=True, blank=True)
#     data_criacao = models.DateTimeField(null=True, blank=True)
#     agendamento_id = models.IntegerField(null=True, blank=True)
#     request_id = models.CharField(unique=True, max_length=45, blank=True)
#     status = models.CharField(max_length=90, blank=True)
#     app_analysis = models.IntegerField(null=True, blank=True)
#     data_conclusao = models.DateTimeField(null=True, blank=True)
#     relatorio_cenzic_id = models.IntegerField(null=True, blank=True)
#     percentual = models.IntegerField(null=True, blank=True)
#     created_at = models.DateTimeField(null=True, blank=True)
#     updated_at = models.DateTimeField(null=True, blank=True)
#     hackalert_id = models.IntegerField(null=True, blank=True)
#     scan_avds_id = models.CharField(max_length=255, blank=True)
#     webscan_avds_id = models.CharField(max_length=255, blank=True)
#     error_description = models.CharField(max_length=255, blank=True)
#     numero_tentativas = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'scans'

class SchemaMigrations(models.Model):
    version = models.CharField(unique=True, max_length=255)
    class Meta:
        db_table = u'schema_migrations'

class Servicos(models.Model):
    
    nome = models.CharField(max_length=60, blank=True)
    descricao = models.CharField(max_length=300, blank=True)
    url = models.CharField(max_length=255, blank=True)
    timeout = models.IntegerField(null=True, blank=True)
    configuracao = models.ForeignKey("Configuracoes", null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'servicos'

class Submissoes(models.Model):
    
    submetido_id = models.IntegerField(null=True, blank=True)
    submetido_type = models.CharField(max_length=255, blank=True)
    cliente = models.ForeignKey("Clientes", null=True, blank=True, related_name="client_submissions")
    adquirente = models.ForeignKey("Adquirentes", null=True, blank=True, related_name="acquirer")
    aceita = models.IntegerField(null=True, blank=True)
    comentario = models.TextField(blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    usuario_submeteu = models.ForeignKey("Usuarios", null=True, blank=True, related_name="user_submitted")
    usuario_aprovou = models.ForeignKey("Usuarios", null=True, blank=True, related_name="user_approved")
    data_aprovacao = models.DateTimeField(null=True, blank=True)
    periodo = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'submissoes'

class Suportes(models.Model):
    
    duvida = models.CharField(max_length=255, blank=True)
    usuario = models.ForeignKey("Usuarios", null=True, blank=True, related_name="user_support")
    arquivo_file_name = models.CharField(max_length=255, blank=True)
    arquivo_content_type = models.CharField(max_length=255, blank=True)
    arquivo_file_size = models.IntegerField(null=True, blank=True)
    arquivo_updated_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    assunto = models.CharField(max_length=255, blank=True)
    cliente = models.ForeignKey("Clientes", null=True, blank=True, related_name="client_support")
    status = models.IntegerField(null=True, blank=True)
    tipo = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'suportes'

class Taggings(models.Model):
    
    tag = models.ForeignKey("Tags", null=True, blank=True)
    taggable_id = models.IntegerField(null=True, blank=True)
    taggable_type = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'taggings'

class Tags(models.Model):
    
    name = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'tags'

# class TipoScans(models.Model):
    
#     nome = models.CharField(max_length=150, blank=True)
#     descricao = models.TextField(blank=True)
#     created_at = models.DateTimeField(null=True, blank=True)
#     updated_at = models.DateTimeField(null=True, blank=True)
#     class Meta:
#         db_table = u'tipo_scans'

class Tokens(models.Model):
    
    key = models.CharField(max_length=255, blank=True)
    usuario = models.ForeignKey("Usuarios", null=True, blank=True)
    type = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'tokens'

class UserProfiles(models.Model):
    
    usuario = models.ForeignKey("Usuarios", null=True, blank=True)
    stamp_enable_disable = models.IntegerField(null=True, blank=True)
    scan_finished = models.IntegerField(null=True, blank=True)
    vulnerability_critic_url = models.IntegerField(null=True, blank=True)
    vulnerability_critic_ip = models.IntegerField(null=True, blank=True)
    news_functions_information = models.IntegerField(null=True, blank=True)
    newsletter = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    feed = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'user_profiles'

class Usuarios(models.Model):
    
    nome = models.CharField(max_length=255, blank=True)
    crypted_password = models.CharField(max_length=120, blank=True)
    salt = models.CharField(max_length=120, blank=True, null=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    remember_token = models.CharField(max_length=120, blank=True, null=True)
    remember_token_expires_at = models.DateTimeField(null=True, blank=True)
    activation_code = models.CharField(max_length=120, blank=True, null=True)
    activated_at = models.DateTimeField(null=True, blank=True)
    login = models.CharField(max_length=255, blank=True)
    emergencia = models.IntegerField(null=True, blank=True)
    admin = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=255)
    reset_code = models.CharField(max_length=255, blank=True)
    concordo = models.IntegerField(null=True, blank=True)
    num_acessos = models.IntegerField(null=True, blank=True)
    ultimo_acesso = models.DateTimeField(null=True, blank=True)
    telefone = models.CharField(max_length=255, blank=True)
    cpf = models.CharField(max_length=255)
    termo_de_uso_aceito_at = models.DateTimeField(null=True, blank=True)
    tentativas_falhas = models.IntegerField(null=True, blank=True)
    ultima_tentativa = models.DateTimeField(null=True, blank=True)
    adquirente = models.ForeignKey("Adquirentes", null=True, blank=True)
    proprietario = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'usuarios'

# class Vulnerabilidades(models.Model):
    
#     qid = models.IntegerField(null=True, blank=True)
#     vuln_type = models.CharField(max_length=255, blank=True)
#     severity_level = models.IntegerField(null=True, blank=True)
#     title = models.CharField(max_length=255, blank=True)
#     category = models.CharField(max_length=255, blank=True)
#     last_update = models.DateTimeField(null=True, blank=True)
#     diagnosis = models.TextField(blank=True)
#     consequence = models.TextField(blank=True)
#     solution = models.TextField(blank=True)
#     created_at = models.DateTimeField(null=True, blank=True)
#     updated_at = models.DateTimeField(null=True, blank=True)
#     class Meta:
#         db_table = u'vulnerabilidades'

