import os 
import sqlite3
from pessoa import Pessoa
from marca import Marca
from Veiculo import Vehiculo

class BancoDeDados:
    def __init__(self,nome_banco="banco.sqlite"):
        self.nome_banco= os.path.join(os.path.dirname(__file__),nome_banco)
        self.conn= nome_banco


    def concex(self):
        try:
            self.conn=sqlite3.conncet(self.nome_banco)
        except sqlite3.Error as e:
            print(f'erro ao conectar: {e}')

    def criar_tabelas(self):
        self.criar_tabela_pessoa()
        self.criar_tabela_marca()
        self.criar_tabela_carro()

    def criar_tabela_pessoa():
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Pessoa(
                        cpf INTEGER PRIMARY KEY,
                        nome TEXT NOT NULL,
                        nascimento DATE,
                        oculos BOOLEAN
                    )"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"erro ao criar tabela pessoa: {e}")
                
    def criar_tabela_marca():
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Marca(
                        id INTEGER PRIMARY KEY,
                        nome TEXT NOT NULL,
                        sigla TEXT,
                        )"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"erro ao criar tabela Marca: {e}")

    def criar_tabela_veiculo():
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Veiculo(
                       placa TEXT PRIMARY KEY,
                       cor TEXT NOT NULL,
                       FOREGIN KEY (cpf_proprietario) REFERENCES Pessoa(cpd),
                       FOREGIN KEY (id_marca) REFERENCES Marca(id)
                    )"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"erro ao criar tabela veiculo: {e}")
