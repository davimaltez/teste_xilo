from django.apps import AppConfig
from django.contrib.admin import apps as admin_apps


class LojaConfig(AppConfig):
    name = 'loja'


class VeredasAdminConfig(admin_apps.AdminConfig):
    default = False
    default_site = 'loja.admin_site.VeredasAdminSite'
