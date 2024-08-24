from django.db import models

# Create your models here.
class Parameters(models.Model):
    impostos = models.FloatField()
    retirada = models.FloatField()
    frete = models.FloatField()
    comissao = models.FloatField()
    lucro = models.FloatField()
    divisor = models.FloatField()

    def __str__(self):
        return self.divisor
    
    def get_divisor(self):
        pass

