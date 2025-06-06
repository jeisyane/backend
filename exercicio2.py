class Funcionario:
    def calcular_pagamento(self):
       pass


class Coordenador(Funcionario):
    def calcular_pagamento(self):
        return 8000


class Desenvolvedor(Funcionario):
    def calcular_pagamento(self):
        return 5000


class Estagiario(Funcionario):
    def calcular_pagamento(self):
        return 1500

lista_funcionarios= [Coordenador() , Desenvolvedor(), Estagiario()]

for funcionario in pagamento:
    print("Pagamento: R${funcionario.calcular_pagamento()}")

