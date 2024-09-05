from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .repository import *

class CollectionService:

    @staticmethod
    def list_all_collections(page=1, per_page=10):
        all_collections = CollectionRepository.get_all_collections()
        paginator = Paginator(all_collections, per_page)

        try:
            collections = paginator.page(page)
        except PageNotAnInteger:
            collections = paginator.page(1)
        except EmptyPage:
            collections = paginator.page(paginator.num_pages)

        return collections
    
    @staticmethod
    def get_all_collections():
        return CollectionRepository.get_all_collections()

    def get_last_4_collections():
        return CollectionRepository.get_last_4(limit=4)

    @staticmethod
    def get_collection_by_id(id):
        return CollectionRepository.get_collection_by_id(id)

    @staticmethod
    def create_collection(name, description, image):
        return CollectionRepository.create_collection(name, description, image)

    @staticmethod
    def update_collection(id_collection, name, description, image):
        return CollectionRepository.update_collection(id_collection, name, description, image)

    @staticmethod
    def delete_collection(id_collection):
        return CollectionRepository.delete_collection(id_collection)

    @staticmethod
    def search_collection(search_query):
        return CollectionRepository.search_collection(search_query)