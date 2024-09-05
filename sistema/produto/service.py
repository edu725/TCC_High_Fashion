from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .repository import *

class ProductService():

    @staticmethod
    def list_all_products(page=1, per_page=12):
        all_products = ProductRepository.get_all_products()
        paginator = Paginator(all_products, per_page)

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        return products
    
    
    @staticmethod
    def get_products_by_collection(id_collection):
        return ProductRepository.get_product_by_collection(id_collection)
    
    @staticmethod
    def get_all_products():
        return ProductRepository.get_all_products()
    
    @staticmethod
    def get_last_product():
        return ProductRepository.get_last_product()
    
    @staticmethod
    def get_last_8():
        return ProductRepository.get_last_8(limit=8)

    @staticmethod
    def get_product_by_id(product_id):
        return ProductRepository.get_product_by_id(product_id)
    
    @staticmethod
    def create_product(name, description, type, path, collection):
        return ProductRepository.create_product(name, description, type, collection, path)

    @staticmethod
    def update_product(id_product, name, description, type, collection, path):
        return ProductRepository.update_product(id_product, name, description, type, collection, path)

    @staticmethod
    def delete_product(id_product):
        return ProductRepository.delete_product(id_product)
    
class ProductCostService:

    @staticmethod
    def create_product_cost(product, parameters, raw_materials, labor, indirect):
        return ProductCostRepository.create_product_cost(product, parameters, raw_materials, labor, indirect)
    
    @staticmethod
    def get_id_fk(fk):
        return ProductCostRepository.get_id_fk(fk)

class CommentProductService():

    @staticmethod
    def list_all_comments(id_product):
        return CommentProductRepository.get_all_comments_product(id_product)
    
    def create_comment_product(id_product, id_user, comment):
        return CommentProductRepository.create_comment_product(id_product, id_user, comment)

    def delete_comment_product( id_comment):
        return CommentProductRepository.delete_comment_product( id_comment)  

    def update_comment_product(id_comment, id_product, id_user,comment):
        return CommentProductRepository.update_comment_product(id_comment, id_product, id_user, comment)
    
class CommentPageService():

    @staticmethod
    def create_comment_page(id_user, comment):
        return CommentPageRepository.create_comment_page(id_user, comment)

    @staticmethod
    def delete_comment_page(id_comment):
        return CommentPageRepository.delete_comment_page(id_comment)
    
    @staticmethod
    def get_all_comments():
        return CommentPageRepository.get_all_comments_page()

    @staticmethod
    def list_all_comments_page(page, per_page=12):
        all_comments = CommentPageRepository.get_all_comments_page()
        paginator = Paginator(all_comments, per_page)

        try:
            comments = paginator.page(page)
        except PageNotAnInteger:
            comments = paginator.page(1)
        except EmptyPage:
            comments = paginator.page(paginator.num_pages)

        return comments
    
