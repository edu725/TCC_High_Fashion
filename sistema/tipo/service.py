from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .repository import *

class TypeService:
    @staticmethod
    def list_all_types(page=1, per_page=10):
        all_types = TypeRepository.get_all_types()
        paginator = Paginator(all_types, per_page)

        try:
            types = paginator.page(page)
        except PageNotAnInteger:
            types = paginator.page(1)
        except EmptyPage:
            types = paginator.page(paginator.num_pages)

        return types
    
    @staticmethod
    def create_new_type(name):
        return TypeRepository.create_type(name)

    @staticmethod
    def update_existing_type(type_id, name):
        return TypeRepository.update_type(type_id, name)

    @staticmethod
    def delete_type(type_id):
        return TypeRepository.delete_type(type_id)
    
    @staticmethod
    def get_all_types():
        return TypeRepository.get_all_types()
    
    @staticmethod
    def search_type(query, page=1, per_page=10):
        types = TypeRepository.search_type(query)
        paginator = Paginator(types, per_page)

        try:
            paginated_types = paginator.page(page)
        except PageNotAnInteger:
            paginated_types = paginator.page(1)
        except EmptyPage:
            paginated_types = paginator.page(paginator.num_pages)

        return paginated_types
    