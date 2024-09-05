from .models import *
from parametros.repository import *


class ProductRepository:

    @staticmethod
    def get_product_by_id(product_id):
        """Retorna os produtos por id"""
        return Product.objects.get(id=product_id)
    
    @staticmethod
    def get_last_product():
        """Retorna o ultimo produto"""
        return Product.objects.order_by('id').last
    
    @staticmethod
    def get_product_by_collection(id_collection):
        """Retorna o ultimo produto"""
        return Product.objects.filter(collection=id_collection)
        
    @staticmethod
    def get_all_products():
        """Retorna todos os produtos"""
        return Product.objects.all()

    @staticmethod
    def get_last_8(limit=8):
        return Product.objects.all().order_by('-id')[:limit]

    @staticmethod
    def create_product(name, description, type, collection, path):
        """Cria um produto"""
        return Product.objects.create(name=name, description=description, type=type, collection=collection, path=path) 

    @staticmethod
    def update_product(id_product, name, description, type, collection, path):
        """Atualizar um produto"""
        product = ProductRepository.get_product_by_id(id_product)
        if product:
            product.name = name
            product.description = description
            product.type = type
            product.collection = collection
            product.path = path
            product.save()
            return True
        else:
            return False

    @staticmethod
    def delete_product(product_id):
        """Deletar um produto"""
        try:
            product = ProductRepository.get_product_by_id(product_id)
            product.delete()
            return True
        except Product.DoesNotExist:
            return False

class ProductCostRepository:

    @staticmethod
    def create_product_cost(product, parameters, raw_materials, labor, indirect):
        return ProductCost.objects.create(product=product, parameters=parameters, raw_materials=raw_materials, labor=labor, indirect=indirect)
    
    @staticmethod
    def get_id_fk(fk):
        return ProductCost.objects.get(product=fk)

class CommentProductRepository:
    @staticmethod
    def create_comment_product(id_product, id_user, comment):
        """ um produto"""
        return CommentProduct.objects.create(id_product=id_product, id_user=id_user, comment=comment)
    
    @staticmethod
    def delete_comment_product(id_comment):
        try:
            comment = CommentProduct.objects.get( id=id_comment )
            comment.delete()
            return True
        except CommentProduct.DoesNotExist:
            return False
    
    @staticmethod
    def get_all_comments_product(id_product):
        return CommentProduct.objects.filter(id_product=id_product)
    
    @staticmethod
    def update_comment_product(id_comment, id_product, id_user, comment):
        try:
            comment = CommentProduct.objects.get( id=id_comment )   
            comment.comment = comment
            comment.id_user = id_user
            comment.id_product = id_product
            comment.save()
            return True
        except CommentProduct.DoesNotExist:
            return False
    
    
class CommentPageRepository:

    @staticmethod
    def get_all_comments_page():
        return CommentPage.objects.all()
    
    @staticmethod
    def create_comment_page(id_user, comment):
        return CommentPage.objects.create(id_user=id_user, comment=comment)

    @staticmethod
    def delete_comment_page(id_comment):
        try:
            comment = CommentPage.objects.get(id=id_comment)
            comment.delete()
            return True
        except CommentPage.DoesNotExist:
            return False
