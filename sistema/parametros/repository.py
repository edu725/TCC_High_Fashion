from .models import *

class ParametersRepository:

    @staticmethod
    def get_id_parameter():
        return Parameters.objects.get(id=1)

    @staticmethod
    def update_parameter(impostos, retirada, frete, comissao, despesas_financeiras, despesas_comerciais, lucro):
        parameter = ParametersRepository.get_id_parameter()
        if parameter:
            parameter.impostos = impostos
            parameter.retirada = retirada
            parameter.frete = frete
            parameter.comissao = comissao
            parameter.despesas_financeiras = despesas_financeiras
            parameter.despesas_comerciais = despesas_comerciais
            parameter.lucro = lucro
            parameter.save()
            return True
        else:
            return False
