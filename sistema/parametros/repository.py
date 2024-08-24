from .models import *

class ParametersRepository:
    def get_divisor(self):
        return Parameters.objects.get()
