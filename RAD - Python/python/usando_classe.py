from datetime import date
from pessoa import Pessoa
from marca import Marca
from veiculo import Veiculo

# Criando uma instância de Pessoa
pessoa1 = Pessoa(cpf =12345678900,nome="Raphael",nascimento=date(1984,7,26),oculos=True)

#Criando uma instância de Marca

marca1 = Marca(id=1,nome="Fiat",sigla="FIA")

#Criando uma instância de Veiculo

veiculo1 = Veiculo(placa="LRW1I27",cor = "Cinza",proprietario= pessoa1,marca=marca1)