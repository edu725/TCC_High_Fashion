from .models import *

class TypeRepository:
    @staticmethod
    def get_all_types():
        return Type.objects.all()
    
    @staticmethod
    def get_id_type(type_id):
        return Type.objects.get(id = type_id)
    
    @staticmethod
    def delete_type(type_id):
        try:
            type = TypeRepository.get_id_type(type_id)
            type.delete()
            return True
        except Type.DoesNotExist:
            return False
        
    @staticmethod
    def create_type(name):
        return Type.objects.create(name=name)
    
    @staticmethod
    def update_type(type_id, name):
        try:
            type = TypeRepository.get_id_type(type_id)
            type.name = name
            type.save()
            return True
        except Type.DoesNotExist:
            return False
