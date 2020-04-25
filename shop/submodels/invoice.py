from django.db import models


class Invoice(models.Model):
    order = models.ForeignKey('Order', related_name='invoices', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pk