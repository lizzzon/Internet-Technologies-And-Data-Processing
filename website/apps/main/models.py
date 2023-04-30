from django.db import models

class Products(models.Model):
    """"""
    title = models.CharField(max_length=50)
    info = models.CharField(max_length=500)
    img = models.ImageField(upload_to="website/static/assets/shop/products")
    price = models.DecimalField(decimal_places=2, max_digits=6)

