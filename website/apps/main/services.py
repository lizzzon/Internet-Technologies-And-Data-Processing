from apps.main.models import Products


class ProductHandler:
    @staticmethod
    def get_products():
        return Products.objects.all()
