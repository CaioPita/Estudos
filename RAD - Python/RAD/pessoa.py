from dataclasses import dataclass
from datetime import date

@dataclass
class Pessoa:
    cpf: int
    nome: str
    oculos: bool
    nascimento: date
    
    