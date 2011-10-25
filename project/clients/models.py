# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

# class Adquirentes(models.Model):
#     id = models.IntegerField(primary_key=True)
#     nome = models.CharField(unique=True, max_length=255, blank=True)
#     logo = models.CharField(max_length=765, blank=True)
#     cliente_id = models.IntegerField(null=True, blank=True)
#     created_at = models.DateTimeField(null=True, blank=True)
#     updated_at = models.DateTimeField(null=True, blank=True)
#     max_num_ips_pci = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'adquirentes'

class Agendamentos(models.Model):
    id = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=300, blank=True)
    url = models.CharField(max_length=300, blank=True)
    tipo = models.CharField(max_length=60, blank=True)
    frequencia = models.CharField(max_length=60, blank=True)
    inicio_do_agendamento = models.DateTimeField(null=True, blank=True)
    fim_do_agendamento = models.DateTimeField(null=True, blank=True)
    hora_do_scan = models.TextField(blank=True) # This field type is a guess.
    ativo = models.IntegerField(null=True, blank=True)
    data_criacao = models.DateTimeField(null=True, blank=True)
    usuario_id = models.IntegerField(null=True, blank=True)
    client_id = models.CharField(max_length=45, blank=True)
    dispositivo_id = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=90, blank=True)
    app_analysis = models.IntegerField(null=True, blank=True)
    tipo_scan_id = models.IntegerField(null=True, blank=True)
    data_conclusao = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    provedor_utilizado = models.CharField(max_length=765, blank=True)
    dispositivo_malware_id = models.IntegerField(null=True, blank=True)
    dia_scan_mensal = models.IntegerField(null=True, blank=True)
    recorrente = models.IntegerField(null=True, blank=True)
    dia_scan_semanal = models.IntegerField(null=True, blank=True)
    ultimo_scan_criado = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'agendamentos'

class Assinaturas(models.Model):
    id = models.IntegerField(primary_key=True)
    cliente_id = models.IntegerField()
    plano_id = models.IntegerField()
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    ativa = models.IntegerField(null=True, blank=True)
    data_rescisao = models.DateField(null=True, blank=True)
    type = models.CharField(max_length=765, blank=True)
    assinatura_base_id = models.IntegerField(null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'assinaturas'

class AtaqueItens(models.Model):
    id = models.IntegerField(primary_key=True)
    ataque_id = models.IntegerField(null=True, blank=True)
    tipo = models.CharField(max_length=150, blank=True)
    severidade = models.CharField(max_length=150, blank=True)
    url = models.CharField(max_length=450, blank=True)
    mensagem = models.TextField(blank=True)
    data_criacao = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    http_request = models.TextField(blank=True)
    http_response = models.TextField(blank=True)
    class Meta:
        db_table = u'ataque_itens'

class Ataques(models.Model):
    id = models.IntegerField(primary_key=True)
    relatorio_cenzic_id = models.IntegerField(null=True, blank=True)
    nome = models.CharField(max_length=300, blank=True)
    descricao = models.TextField(blank=True)
    como_funciona = models.TextField(blank=True)
    impacto = models.TextField(blank=True)
    solucao = models.TextField(blank=True)
    nivel = models.IntegerField(null=True, blank=True)
    tipo = models.TextField(blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    test_id = models.IntegerField(null=True, blank=True)
    reference = models.TextField(blank=True)
    avds_vulnerabilidade_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'ataques'

class AvdsVulnerabilidades(models.Model):
    id = models.IntegerField(primary_key=True)
    family = models.CharField(max_length=15000, blank=True)
    name = models.CharField(max_length=15000, blank=True)
    description = models.CharField(max_length=15000, blank=True)
    how_it_works = models.CharField(max_length=15000, blank=True)
    impact = models.CharField(max_length=15000, blank=True)
    solution = models.CharField(max_length=15000, blank=True)
    risk = models.IntegerField(null=True, blank=True)
    test_id = models.IntegerField(null=True, blank=True)
    service = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'avds_vulnerabilidades'

class Blacklists(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'blacklists'

# class Clientes(models.Model):
#     id = models.IntegerField(primary_key=True)
#     type = models.CharField(max_length=765)
#     nome = models.CharField(max_length=765)
#     cpf = models.CharField(max_length=765, blank=True)
#     cnpj = models.CharField(max_length=765, blank=True)
#     inscricao_estadual = models.CharField(max_length=765, blank=True)
#     email = models.CharField(max_length=765, blank=True)
#     cep = models.CharField(max_length=765, blank=True)
#     endereco = models.TextField(blank=True)
#     bairro = models.CharField(max_length=765, blank=True)
#     cidade = models.CharField(max_length=765, blank=True)
#     estado = models.CharField(max_length=765, blank=True)
#     telefone = models.CharField(max_length=765, blank=True)
#     fax = models.CharField(max_length=765, blank=True)
#     celular = models.CharField(max_length=765, blank=True)
#     ativo = models.IntegerField(null=True, blank=True)
#     created_at = models.DateTimeField(null=True, blank=True)
#     updated_at = models.DateTimeField(null=True, blank=True)
#     rg = models.CharField(max_length=765, blank=True)
#     descricao = models.TextField(blank=True)
#     observacoes = models.TextField(blank=True)
#     url = models.CharField(max_length=765, blank=True)
#     segmento = models.IntegerField(null=True, blank=True)
#     logo_file_name = models.CharField(max_length=765, blank=True)
#     logo_content_type = models.CharField(max_length=765, blank=True)
#     logo_file_size = models.IntegerField(null=True, blank=True)
#     logo_updated_at = models.DateTimeField(null=True, blank=True)
#     representante_nome = models.CharField(max_length=765, blank=True)
#     representante_email = models.CharField(max_length=765, blank=True)
#     representante_rg = models.CharField(max_length=765, blank=True)
#     representante_cpf = models.CharField(max_length=765, blank=True)
#     activation_code = models.CharField(max_length=765, blank=True)
#     activated_at = models.DateTimeField(null=True, blank=True)
#     tipo_questionario = models.CharField(max_length=765, blank=True)
#     nivel = models.IntegerField(null=True, blank=True)
#     provedor_scan = models.IntegerField(null=True, blank=True)
#     provedor_scan_ip = models.IntegerField(null=True, blank=True)
#     online = models.IntegerField(null=True, blank=True)
#     numero = models.IntegerField(null=True, blank=True)
#     complemento_endereco = models.CharField(max_length=765, blank=True)
#     proprietario = models.IntegerField(null=True, blank=True)
#     tipo_retorno_por_cep = models.IntegerField(null=True, blank=True)
#     sid = models.CharField(max_length=48, blank=True)
#     vip_client = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'clientes'

class ClientesGrupos(models.Model):
    cliente_id = models.IntegerField(null=True, blank=True)
    grupo_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'clientes_grupos'

class Configuracoes(models.Model):
    # id = models.IntegerField(null=True, blank=True)
    nome = models.CharField(max_length=300, blank=True)
    descricao = models.CharField(max_length=300, blank=True)
    frequencia = models.IntegerField(null=True, blank=True)
    timeout = models.IntegerField(null=True, blank=True)
    nr_max_scans = models.IntegerField(null=True, blank=True)
    param1 = models.CharField(max_length=300, blank=True)
    param2 = models.CharField(max_length=300, blank=True)
    param3 = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'configuracoes'

class Consultas(models.Model):
    id = models.IntegerField(primary_key=True)
    ip_requisicao = models.CharField(max_length=765, blank=True)
    nome = models.CharField(max_length=765, blank=True)
    email = models.CharField(max_length=765, blank=True)
    dominio = models.CharField(max_length=765, blank=True)
    blindado = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'consultas'

class Contratos(models.Model):
    id = models.IntegerField(primary_key=True)
    cliente_id = models.IntegerField(null=True, blank=True)
    m_plano_id = models.IntegerField(null=True, blank=True)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    ativo = models.IntegerField(null=True, blank=True)
    data_rescisao = models.DateField(null=True, blank=True)
    tipo = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'contratos'

class DashboardDeviceAndVulrenabilitys(models.Model):
    id = models.IntegerField(primary_key=True)
    device_id = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    object_type = models.CharField(max_length=765, blank=True)
    object_id = models.IntegerField(null=True, blank=True)
    object_data = models.CharField(max_length=1500, blank=True)
    class Meta:
        db_table = u'dashboard_device_and_vulrenabilitys'

class DashboardStats(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    nivel_1 = models.IntegerField(null=True, blank=True)
    nivel_2 = models.IntegerField(null=True, blank=True)
    nivel_3 = models.IntegerField(null=True, blank=True)
    nivel_4 = models.IntegerField(null=True, blank=True)
    nivel_5 = models.IntegerField(null=True, blank=True)
    cliente_id = models.IntegerField(null=True, blank=True)
    report_date = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'dashboard_stats'

class DashboardTops(models.Model):
    id = models.IntegerField(primary_key=True)
    quantity = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    object_type = models.CharField(max_length=765, blank=True)
    object_id = models.IntegerField(null=True, blank=True)
    object_data = models.CharField(max_length=1500, blank=True)
    class Meta:
        db_table = u'dashboard_tops'

# class Dispositivos(models.Model):
#     id = models.IntegerField(primary_key=True)
#     nome = models.CharField(max_length=765, blank=True)
#     type = models.CharField(max_length=765, blank=True)
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
#     alias = models.CharField(max_length=765, blank=True)
#     idioma_selo = models.CharField(max_length=765, blank=True)
#     description = models.CharField(max_length=1500, blank=True)
#     dispositivo_logo_file_name = models.CharField(max_length=765, blank=True)
#     dispositivo_logo_content_type = models.CharField(max_length=765, blank=True)
#     dispositivo_logo_file_size = models.IntegerField(null=True, blank=True)
#     dispositivo_logo_updated_at = models.DateTimeField(null=True, blank=True)
#     class Meta:
#         db_table = u'dispositivos'

# class DispositivosMalware(models.Model):
#     id = models.IntegerField(primary_key=True)
#     nome = models.CharField(max_length=765, blank=True)
#     alias = models.CharField(max_length=765, blank=True)
#     type = models.CharField(max_length=765, blank=True)
#     cliente_id = models.IntegerField(null=True, blank=True)
#     certificado = models.IntegerField(null=True, blank=True)
#     ativo = models.IntegerField(null=True, blank=True)
#     quantidade_links = models.IntegerField(null=True, blank=True)
#     created_at = models.DateTimeField(null=True, blank=True)
#     updated_at = models.DateTimeField(null=True, blank=True)
#     quantidade_links_adicionais = models.IntegerField(null=True, blank=True)
#     selo_id = models.IntegerField(null=True, blank=True)
#     removido = models.IntegerField(null=True, blank=True)
#     trial_bloqueado = models.IntegerField(null=True, blank=True)
#     liberar_selo = models.IntegerField()
#     class Meta:
#         db_table = u'dispositivos_malware'

class EstatisticaContas(models.Model):
    # id = models.IntegerField(primary_key=True)
    clientes_count = models.IntegerField(null=True, blank=True)
    contas_ativas_count = models.IntegerField(null=True, blank=True)
    ips_disponiveis = models.IntegerField(null=True, blank=True)
    ips_cadastrados = models.IntegerField(null=True, blank=True)
    scans_realizados = models.IntegerField(null=True, blank=True)
    adquirente_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    max_num_ips_pci = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'estatistica_contas'

class Estatisticas(models.Model):
    # id = models.IntegerField()
    page_views = models.IntegerField(null=True, blank=True)
    banda = models.IntegerField(null=True, blank=True)
    dispositivo_id = models.IntegerField(null=True, blank=True)
    mes_ano = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    page_views_akamai = models.IntegerField(null=True, blank=True)
    banda_akamai = models.IntegerField(null=True, blank=True)
    dispositivo_malware_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'estatisticas'

class FeedReports(models.Model):
    id = models.IntegerField(primary_key=True)
    feed_id = models.IntegerField(null=True, blank=True)
    _report_id = models.IntegerField(null=True, blank=True)
    _report_type = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'feed_reports'

class Feeds(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario_id = models.IntegerField(null=True, blank=True)
    private_key = models.CharField(max_length=765, blank=True)
    title = models.CharField(max_length=765, blank=True)
    slug = models.CharField(max_length=765, blank=True)
    content = models.CharField(max_length=30000, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'feeds'

class Grupos(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=765, blank=True)
    adquirente_id = models.IntegerField(null=True, blank=True)
    quinzenas = models.CharField(max_length=765, blank=True)
    ativo = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'grupos'

class HaProfilingReports(models.Model):
    id = models.IntegerField(primary_key=True)
    data = models.TextField(blank=True)
    scan_status_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'ha_profiling_reports'

class HaScanStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    scan_request_id = models.IntegerField(null=True, blank=True)
    scan_result_id = models.IntegerField(null=True, blank=True)
    scan_request_hostname = models.CharField(max_length=765, blank=True)
    scan_started_at = models.DateTimeField(null=True, blank=True)
    scan_completed_at = models.DateTimeField(null=True, blank=True)
    scan_hostname = models.CharField(max_length=765, blank=True)
    entrypoint = models.CharField(max_length=765, blank=True)
    status = models.CharField(max_length=765, blank=True)
    failure_code = models.CharField(max_length=765, blank=True)
    failure_reason = models.CharField(max_length=765, blank=True)
    internal_pages_scanned = models.IntegerField(null=True, blank=True)
    external_pages_scanned = models.IntegerField(null=True, blank=True)
    http_pages_scanned = models.IntegerField(null=True, blank=True)
    https_pages_scanned = models.IntegerField(null=True, blank=True)
    scan_time = models.IntegerField(null=True, blank=True)
    estimated_time_of_completion = models.DateTimeField(null=True, blank=True)
    position_in_queue = models.IntegerField(null=True, blank=True)
    scan_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'ha_scan_status'

class HaScannedUrls(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=765, blank=True)
    blacklisted_data = models.TextField(blank=True)
    malicious_data = models.TextField(blank=True)
    suspicious_data = models.TextField(blank=True)
    scan_status_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'ha_scanned_urls'

class LogonImages(models.Model):
    id = models.IntegerField(primary_key=True)
    caption = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    picture_file_name = models.CharField(max_length=765, blank=True)
    picture_content_type = models.CharField(max_length=765, blank=True)
    picture_file_size = models.IntegerField(null=True, blank=True)
    picture_updated_at = models.DateTimeField(null=True, blank=True)
    link = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'logon_images'

class Logs(models.Model):
    id = models.IntegerField(primary_key=True)
    erro = models.CharField(max_length=1500, blank=True)
    mensagem = models.CharField(max_length=1500, blank=True)
    trace = models.CharField(max_length=3000, blank=True)
    scan_id = models.IntegerField(null=True, blank=True)
    data_criacao = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'logs'

class MContratos(models.Model):
    id = models.IntegerField(primary_key=True)
    cliente_id = models.IntegerField(null=True, blank=True)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    ativo = models.IntegerField(null=True, blank=True)
    data_rescisao = models.DateField(null=True, blank=True)
    tipo = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    trial = models.IntegerField(null=True, blank=True)
    sf_contrato_cod = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'm_contratos'

class MContratosPlanos(models.Model):
    id = models.IntegerField(primary_key=True)
    m_contrato_id = models.IntegerField()
    m_plano_id = models.IntegerField()
    dispositivo_malware_id = models.IntegerField()
    valor_plano = models.DecimalField(max_digits=10, decimal_places=2)
    valor_links_adicionais = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'm_contratos_planos'

class MPlanoFaixas(models.Model):
    id = models.IntegerField(primary_key=True)
    m_plano_id = models.IntegerField()
    quantidade_links = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    sf_servico_cod = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'm_plano_faixas'

class MPlanos(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=765)
    descricao = models.CharField(max_length=765)
    num_urls = models.IntegerField()
    periodicidade = models.CharField(max_length=765)
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
    id = models.IntegerField(primary_key=True)
    usuario_id = models.IntegerField()
    acao = models.CharField(max_length=765)
    dispositivo = models.CharField(max_length=765, blank=True)
    justificativa = models.TextField(blank=True)
    cliente_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'movimentacoes'

class Notifications(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=765, blank=True)
    preview = models.TextField(blank=True)
    link = models.CharField(max_length=765, blank=True)
    publication = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'notifications'

class Perguntas(models.Model):
    id = models.IntegerField(primary_key=True)
    texto = models.TextField(blank=True)
    requisito_id = models.IntegerField(null=True, blank=True)
    questionario_id = models.IntegerField(null=True, blank=True)
    dica = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    titulo = models.IntegerField(null=True, blank=True)
    pergunta_mae_id = models.IntegerField(null=True, blank=True)
    numero = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'perguntas'

class Permissoes(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario_id = models.IntegerField()
    cliente_id = models.IntegerField()
    papel = models.IntegerField()
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'permissoes'

class Pesquisas(models.Model):
    id = models.IntegerField(primary_key=True)
    data_inicio = models.DateTimeField(null=True, blank=True)
    data_fim = models.DateTimeField(null=True, blank=True)
    dispositivo_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    vendas_desde_ultimo_email = models.IntegerField(null=True, blank=True)
    ultimo_email_enviado = models.DateTimeField(null=True, blank=True)
    envia_email_finalizado = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=765, blank=True)
    codigo_promocional = models.CharField(max_length=765, blank=True)
    resultado_pesquisa_menor_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'pesquisas'

class Planos(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=765)
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
    type = models.CharField(max_length=765, blank=True)
    usa_selo_akamai = models.IntegerField(null=True, blank=True)
    num_ips_pci = models.IntegerField(null=True, blank=True)
    plano_site_blindado = models.TextField(blank=True) # This field type is a guess.
    plano_malware_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'planos'

class QuestionarioClientes(models.Model):
    id = models.IntegerField(primary_key=True)
    questionario_id = models.IntegerField(null=True, blank=True)
    cliente_id = models.IntegerField(null=True, blank=True)
    respostas_count = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    nome = models.CharField(max_length=765, blank=True)
    dbas = models.CharField(max_length=765, blank=True)
    contato = models.CharField(max_length=765, blank=True)
    tipos_negocio = models.TextField(blank=True)
    relacionamento_prestadores_servico = models.IntegerField(null=True, blank=True)
    relacionamento_adquirente = models.IntegerField(null=True, blank=True)
    aplicativo_pagamento = models.CharField(max_length=765, blank=True)
    versao_aplicativo_pagamento = models.CharField(max_length=765, blank=True)
    questionario_preenchido = models.IntegerField(null=True, blank=True)
    informacoes_representam_resultados = models.IntegerField(null=True, blank=True)
    confirmacao_nao_armazenamento_dados_autenticacao = models.IntegerField(null=True, blank=True)
    reconhecimento_conformidade_total = models.IntegerField(null=True, blank=True)
    sem_evidencias_armazenamento_dados = models.IntegerField(null=True, blank=True)
    responsavel_executivo = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'questionario_clientes'

class Questionarios(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=765, blank=True)
    ativo = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'questionarios'

class Referencias(models.Model):
    id = models.IntegerField(primary_key=True)
    vulnerabilidade_id = models.IntegerField(null=True, blank=True)
    tipo = models.CharField(max_length=765, blank=True)
    url = models.CharField(max_length=765, blank=True)
    rid = models.CharField(max_length=765, blank=True)
    description = models.TextField(blank=True)
    section = models.CharField(max_length=765, blank=True)
    compliance_type = models.CharField(max_length=765, blank=True)
    info = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'referencias'

class RelatorioCenzics(models.Model):
    id = models.IntegerField(primary_key=True)
    duracao = models.IntegerField(null=True, blank=True)
    data_criacao = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    os = models.CharField(max_length=765, blank=True)
    nameserver = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'relatorio_cenzics'

class RelatorioVulnerabilidades(models.Model):
    id = models.IntegerField(primary_key=True)
    relatorio_id = models.IntegerField(null=True, blank=True)
    vulnerabilidade_id = models.IntegerField(null=True, blank=True)
    result = models.TextField(blank=True)
    tipo = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    format_table = models.IntegerField(null=True, blank=True)
    port = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'relatorio_vulnerabilidades'

class Relatorios(models.Model):
    id = models.IntegerField(primary_key=True)
    scan_ref = models.CharField(max_length=765, blank=True)
    username = models.CharField(max_length=765, blank=True)
    company = models.CharField(max_length=765, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=765, blank=True)
    target = models.CharField(max_length=765, blank=True)
    duration = models.CharField(max_length=765, blank=True)
    scan_host = models.CharField(max_length=765, blank=True)
    nbhost_alive = models.IntegerField(null=True, blank=True)
    nbhost_total = models.IntegerField(null=True, blank=True)
    report_type = models.CharField(max_length=765, blank=True)
    options = models.TextField(blank=True)
    status = models.CharField(max_length=765, blank=True)
    asset_group = models.CharField(max_length=765, blank=True)
    option_profile = models.CharField(max_length=765, blank=True)
    ip = models.CharField(max_length=765, blank=True)
    nameserver = models.CharField(max_length=765, blank=True)
    os = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    atualizado = models.IntegerField(null=True, blank=True)
    dispositivo_id = models.IntegerField(null=True, blank=True)
    cliente_id = models.IntegerField(null=True, blank=True)
    scan_manual = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=765, blank=True)
    merchant_name = models.CharField(max_length=765, blank=True)
    num_hosts_compliant = models.IntegerField(null=True, blank=True)
    compliance_status = models.CharField(max_length=765, blank=True)
    partner_name = models.CharField(max_length=765, blank=True)
    scan_module = models.CharField(max_length=765, blank=True)
    port = models.IntegerField(null=True, blank=True)
    qualys_id_relatorio = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'relatorios'

class Requisitos(models.Model):
    id = models.IntegerField(primary_key=True)
    numero = models.IntegerField(null=True, blank=True)
    descricao = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'requisitos'

class Respostas(models.Model):
    id = models.IntegerField(primary_key=True)
    pergunta_id = models.IntegerField(null=True, blank=True)
    opcao = models.IntegerField(null=True, blank=True)
    comentario = models.TextField(blank=True)
    questionario_cliente_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'respostas'

class ResultadoPesquisas(models.Model):
    id = models.IntegerField(primary_key=True)
    viu_selo = models.IntegerField(null=True, blank=True)
    data_compra = models.DateTimeField(null=True, blank=True)
    compras_duplicadas = models.IntegerField(null=True, blank=True)
    ip = models.CharField(max_length=765, blank=True)
    url_compra = models.CharField(max_length=765, blank=True)
    pesquisa_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    comprou = models.IntegerField(null=True, blank=True)
    preco = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'resultado_pesquisas'

class Scans(models.Model):
    id = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=300, blank=True)
    data_do_scan = models.DateTimeField(null=True, blank=True)
    concluido = models.IntegerField(null=True, blank=True)
    data_criacao = models.DateTimeField(null=True, blank=True)
    agendamento_id = models.IntegerField(null=True, blank=True)
    request_id = models.CharField(unique=True, max_length=45, blank=True)
    status = models.CharField(max_length=90, blank=True)
    app_analysis = models.IntegerField(null=True, blank=True)
    data_conclusao = models.DateTimeField(null=True, blank=True)
    relatorio_cenzic_id = models.IntegerField(null=True, blank=True)
    percentual = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    hackalert_id = models.IntegerField(null=True, blank=True)
    scan_avds_id = models.CharField(max_length=765, blank=True)
    webscan_avds_id = models.CharField(max_length=765, blank=True)
    error_description = models.CharField(max_length=765, blank=True)
    numero_tentativas = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'scans'

class SchemaMigrations(models.Model):
    version = models.CharField(unique=True, max_length=255)
    class Meta:
        db_table = u'schema_migrations'

class Servicos(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=60, blank=True)
    descricao = models.CharField(max_length=300, blank=True)
    url = models.CharField(max_length=600, blank=True)
    timeout = models.IntegerField(null=True, blank=True)
    configuracao_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'servicos'

class Submissoes(models.Model):
    id = models.IntegerField(primary_key=True)
    submetido_id = models.IntegerField(null=True, blank=True)
    submetido_type = models.CharField(max_length=765, blank=True)
    cliente_id = models.IntegerField(null=True, blank=True)
    adquirente_id = models.IntegerField(null=True, blank=True)
    aceita = models.IntegerField(null=True, blank=True)
    comentario = models.TextField(blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    usuario_submeteu_id = models.IntegerField(null=True, blank=True)
    usuario_aprovou_id = models.IntegerField(null=True, blank=True)
    data_aprovacao = models.DateTimeField(null=True, blank=True)
    periodo = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'submissoes'

class Suportes(models.Model):
    id = models.IntegerField(primary_key=True)
    duvida = models.CharField(max_length=765, blank=True)
    usuario_id = models.IntegerField(null=True, blank=True)
    arquivo_file_name = models.CharField(max_length=765, blank=True)
    arquivo_content_type = models.CharField(max_length=765, blank=True)
    arquivo_file_size = models.IntegerField(null=True, blank=True)
    arquivo_updated_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    assunto = models.CharField(max_length=765, blank=True)
    cliente_id = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    tipo = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'suportes'

class Taggings(models.Model):
    id = models.IntegerField(primary_key=True)
    tag_id = models.IntegerField(null=True, blank=True)
    taggable_id = models.IntegerField(null=True, blank=True)
    taggable_type = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'taggings'

class Tags(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'tags'

class TipoScans(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150, blank=True)
    descricao = models.CharField(max_length=600, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'tipo_scans'

class Tokens(models.Model):
    id = models.IntegerField(primary_key=True)
    key = models.CharField(max_length=765, blank=True)
    usuario_id = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'tokens'

class UserProfiles(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario_id = models.IntegerField(null=True, blank=True)
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
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=300, blank=True)
    crypted_password = models.CharField(max_length=120, blank=True)
    salt = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    remember_token = models.CharField(max_length=120, blank=True)
    remember_token_expires_at = models.DateTimeField(null=True, blank=True)
    activation_code = models.CharField(max_length=120, blank=True)
    activated_at = models.DateTimeField(null=True, blank=True)
    login = models.CharField(max_length=300, blank=True)
    emergencia = models.IntegerField(null=True, blank=True)
    admin = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=300)
    reset_code = models.CharField(max_length=765, blank=True)
    concordo = models.IntegerField(null=True, blank=True)
    num_acessos = models.IntegerField(null=True, blank=True)
    ultimo_acesso = models.DateTimeField(null=True, blank=True)
    telefone = models.CharField(max_length=765, blank=True)
    cpf = models.CharField(max_length=765)
    termo_de_uso_aceito_at = models.DateTimeField(null=True, blank=True)
    tentativas_falhas = models.IntegerField(null=True, blank=True)
    ultima_tentativa = models.DateTimeField(null=True, blank=True)
    adquirente_id = models.IntegerField(null=True, blank=True)
    proprietario = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'usuarios'

class Vulnerabilidades(models.Model):
    id = models.IntegerField(primary_key=True)
    qid = models.IntegerField(null=True, blank=True)
    vuln_type = models.CharField(max_length=765, blank=True)
    severity_level = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=765, blank=True)
    category = models.CharField(max_length=765, blank=True)
    last_update = models.DateTimeField(null=True, blank=True)
    diagnosis = models.TextField(blank=True)
    consequence = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'vulnerabilidades'

