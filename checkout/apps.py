from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
     Config Checkout app
    """
    name = 'checkout'

    def ready(self):
        import checkout.signals
