from .models import *

class TypeRepository:
    @staticmethod
    def get_all_types():
        return Type.objects.all()
    
    @staticmethod
    def delete_type(type_id):
        try:
            type = Type.objects.get(id=type_id)
            type.delete()
            return True
        except Type.DoesNotExist:
            return False
        
    @staticmethod
    def create_type(name):
        return Type.objects.create(name)
    
    @staticmethod
    def update_type(type_id, name):
        try:
            type = Type.objects.get(id=type_id)
            type.name = name
            type.save()
            return True
        except Type.DoesNotExist:
            return False
        
    @staticmethod
    def search_type(query):
        try:
            # Primeiro tenta buscar por ID
            if query.isdigit():
                return Type.objects.filter(id=query)
        except ValueError:
            pass
        
        # Se não for um ID válido, busca por nome (convertendo para maiúsculas)
        query_upper = query.upper()
        return Type.objects.filter(name__icontains=query_upper)