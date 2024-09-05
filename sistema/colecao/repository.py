from .models import *

class CollectionRepository:
    @staticmethod
    def get_all_collections():
        return Collection.objects.all()
    
    @staticmethod
    def get_collection_by_id(id):
        return Collection.objects.get(id=id)
    
    @staticmethod
    def create_collection(name, description, image):
        return Collection.objects.create(name=name, description=description, image=image)
    
    @staticmethod
    def get_last_4(limit=4):
        return Collection.objects.all().order_by('-id')[:limit]

    @staticmethod
    def update_collection(id_collection, name, description, image):
        collection = CollectionRepository.get_collection_by_id(id=id_collection)
        if collection:
            collection.name = name
            collection.description = description
            collection.image = image
            collection.save()
            return True
        else:
            return False
    
    @staticmethod
    def delete_collection(id_collection):
        try:
            collection = CollectionRepository.get_collection_by_id(id=id_collection)
            collection.delete()
            return True
        except Collection.DoesNotExist:
            return False
      
    @staticmethod
    def search_collection(search_query):

        # Verifica se o valor é numérico e busca por ID
        if search_query.isdigit():
            return Collection.objects.filter(id=search_query)

        else:
            # Se não for uma data, considera como nome da sala
            return Collection.objects.filter(collection_name__icontains=search_query.upper())