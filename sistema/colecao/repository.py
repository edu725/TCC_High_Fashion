from .models import *
from datetime import datetime

class CollectionRepository:
    @staticmethod
    def get_all_collections():
        return Collection.objects.all()
    
    @staticmethod
    def get_collection_by_id(id):
        return Collection.objects.get(id=id)
    
    @staticmethod
    def create_collection(name, description, id_user):
        return Collection.objects.create(name=name, description=description, id_user=id_user)
    
    @staticmethod
    def update_collection(id_collection, name, description):
        try:
            collection = Collection.objects.get(id=id_collection)
            collection.name = name
            collection.description = description
            collection.save()
            return True
        except Collection.DoesNotExist:
            return False
    
    @staticmethod
    def delete_collection(id_collection):
        try:
            collection = Collection.objects.get(id=id_collection)
            collection.delete()
            return True
        except Collection.DoesNotExist:
            return False
        
    @staticmethod
    def search_collection(search_query):
        collections = Collection.objects.all()

        # Verifica se o valor é numérico e busca por ID
        if search_query.isdigit():
            collections = collections.filter(id=search_query)

        else:
            # Se não for uma data, considera como nome da sala
            collections = collections.filter(collection__name__icontains=search_query.upper())

        return collections
        