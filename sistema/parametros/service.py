from .repository import *

class ParametersService:

    @staticmethod
    def get_id_parameter():
        return ParametersRepository.get_id_parameter()

    @staticmethod
    def update_parameter(impostos, retirada, frete, comissao, despesas_financeiras, despesas_comerciais, lucro):
        return ParametersRepository.update_parameter(impostos, retirada, frete, comissao, despesas_financeiras, despesas_comerciais, lucro)
    
    @staticmethod
    def get_divisor():
        return ParametersRepository.get_divisor()