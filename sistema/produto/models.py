from django.db import models
from users.models import User
from tipo.models import Type
from colecao.models import Collection
from parametros.models import Parameters
from django.db.models import Count

# Create your models here.

    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    path = models.ImageField(upload_to='img/%Y/%m/%d/')

    def __str__(self):
        return self.name
    
    def user_commented(self, user):
        return CommentPage.objects.filter(id_user=user).exists()
    
    def most_commented(self):
       return self.objects.annotate(comment_count=Count('comment')).order_by('-comment_count')[:10]
    
    def product_commented(self, user):
        return CommentProduct.objects.filter(id_product=self, id_user=user).exists()
    
    def get_price(self):
        try:
            # Obter o primeiro ProductCost relacionado ao produto
            product_cost = self.productcost_set.first()  # Ajuste o critério se necessário
            if product_cost:
                return product_cost.get_price()
            else:
                return 0
        except ProductCost.DoesNotExist:
            return 0

class ProductCost(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    parameters = models.ForeignKey(Parameters, on_delete=models.CASCADE)
    raw_materials = models.DecimalField(max_digits=8, decimal_places=2)
    labor = models.DecimalField(max_digits=8, decimal_places=2)
    indirect = models.DecimalField(max_digits=8, decimal_places=2)

    def get_price_cost(self):
        return (self.raw_materials + self.labor + self.indirect)
    
    def get_price(self):
        cost = self.get_price_cost()
        divisor = self.parameters.get_divisor()
        if divisor == 0:
            raise ValueError("Divisor cannot be zero.")
        return cost / divisor

class CommentProduct(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f'{self.id_user} on {self.id_product}'

class CommentPage(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment