from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .repository import *

class ProductService():

    @staticmethod
    def list_all_products(page=1, per_page=10):
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
    def get_all_products():
        return ProductRepository.get_all_products()
    @staticmethod
    def get_last_product():
        return ProductRepository.get_last_product()

    @staticmethod
    def get_product_by_id(id):
        return ProductRepository.get_product_by_id(id)
    
    @staticmethod
    def create_product(name, description, type, path):
        return ProductRepository.create_product(name, description, type, path)

    @staticmethod
    def update_product(id_product, name, description, type, path):
        return ProductRepository.update_product(id_product, name, description, type, path)

    @staticmethod
    def delete_product(id_product):
        return ProductRepository.delete_product(id_product)

    # @staticmethod
    # def search_product(query):
    #     return ProductRepository.search_product(query)
    

class CommentProductService():

    @staticmethod
    def list_all_comments(id_product):
        return CommentProductRepository.get_all_comments_product(id_product)
    
    def create_comment_product(id_product, id_user, comment):
        return CommentProductRepository.create_comment_product(id_product, id_user, comment)

    def delete_comment_product(id_comment):
        return CommentProductRepository.delete_comment_product(id_comment)  
    
class CommentPageService():

    @staticmethod
    def create_comment_page(id_user, comment):
        return CommentPageRepository.create_comment_page(id_user, comment)

    @staticmethod
    def delete_comment_page(id_comment):
        return CommentPageRepository.delete_comment_page(id_comment)
    
    @staticmethod
    def list_all_comments_page(page, per_page=10):
        all_comments = CommentPageRepository.get_all_comments_page()
        paginator = Paginator(all_comments, per_page)

        try:
            comments = paginator.page(page)
        except PageNotAnInteger:
            comments = paginator.page(1)
        except EmptyPage:
            comments = paginator.page(paginator.num_pages)

        return comments