from django.db import models

# Create your models here.
class Parameters(models.Model):
    impostos = models.DecimalField(max_digits=8, decimal_places=2)
    retirada = models.DecimalField(max_digits=8, decimal_places=2)
    frete = models.DecimalField(max_digits=8, decimal_places=2)
    comissao = models.DecimalField(max_digits=8, decimal_places=2)
    despesas_financeiras = models.DecimalField(max_digits=8, decimal_places=2)
    despesas_comerciais = models.DecimalField(max_digits=8, decimal_places=2)
    lucro = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.divisor
    
    def get_divisor(self):
        pass

