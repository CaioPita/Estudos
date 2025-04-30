from datetime import date
from pessoa import Pessoa
from marca import Marca
from Veiculo import Vehiculo

#criar instancia de pessoa

pessoa1= Pessoa(cpf=19383313762,nome="Dayanezinha",nascimento=date(2003,12,31), oculos=False)

marca1=Marca(id=220,nome='Volkswagen',sigla='VW')

veiculo= Vehiculo(placa="rjk8i69", cor="Prata",proprietario= pessoa1,marca=marca1)

print(pessoa1.nascimento)