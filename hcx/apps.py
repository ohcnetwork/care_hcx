from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

PLUGIN_NAME = "hcx"


class HcxConfig(AppConfig):
    name = PLUGIN_NAME
    verbose_name = _("HCX Integration")
