from django.apps import AppConfig


class EntregaProductosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "entrega_productos"

    def ready(self):
        import entrega_productos.signals
