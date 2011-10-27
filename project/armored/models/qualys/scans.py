from armored.models import ArmoredScan


class QualysArmoredScan(ArmoredScan):
    # report = models.OneToOneField(QualysReport, null=True, blank=True)  # relatorio_qualys

    class Meta:
        app_label = 'armored'
