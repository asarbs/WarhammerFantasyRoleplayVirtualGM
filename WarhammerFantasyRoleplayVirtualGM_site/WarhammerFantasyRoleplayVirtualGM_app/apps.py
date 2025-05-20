from django.apps import AppConfig


class WarhammerfantasyroleplayvirtualgmAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'WarhammerFantasyRoleplayVirtualGM_app'

    def ready(self):
        import WarhammerFantasyRoleplayVirtualGM_app.signals