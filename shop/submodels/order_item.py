from django.db import models

class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', related_name='order_items', on_delete=models.CASCADE)
    product_price = models.DecimalField(max_digits=10, decimal_places=0)
    product_count = models.PositiveIntegerField()
    product_cost = models.DecimalField(max_digits=10, decimal_places=0)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pk