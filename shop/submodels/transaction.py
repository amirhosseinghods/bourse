from django.db import models

class Transaction(models.Model):
    STATUS = (
        ('p', 'Pending'),
        ('f', 'Failed'),
        ('c', 'Completed')
    )
    invoice = models.ForeignKey('Invoice', related_name='transactions', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.CharField(max_length = 1, choices = STATUS, default = 'pending')

    def __str__(self):
        return self.pk