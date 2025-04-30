import logging

#configuracao basica do logger
logging.basicConfig(
    filename = "app.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s",
)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)

    self.conexao.commit()
    log_info("Tabelas criadas com sucesso!")
    except sqlite3.IntegrityError as e:
        log_error(f"Erro de integridado ao criar tabelas: {e}")
        raise
    except sqlite3.OperationalError as e:
        log_error(f"Erro operacional ao criar tabelas: {e}")
        raise
    except sqlite3.DatabaseError as e:
        log_error(f"Erro de banco ao criar tabelas: {e}")
        raise
    except sqlite3.Error as e:
        log_error(f"Erro geral do SQlite ao criar tabelas: {e}")
        raise
def insert_pessoa(self,pessoa: Pessoa):
    if self.conn:
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO Pessoa VALUES (? , ? , ? , ?)",
            (pessoa.cpf, pessoa.nome, pessoa.nascimento ,pessoa.oculos),)
                    self.conn.commit()
                except sqlite3.Error as e:
                    print(f"Erro ao inserir pessoa: {e}")
def insert_veiculo(self, veiculo: Veiculo):
    if self.conn:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO Veiculo VALUES (?, ?, ?, ?)",
                (
                    veiculo.placa,
                    veiculo.cor,
                    veiculo.proprietario.cpf,
                    veiculo.marca.id,
                ),
            )
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao inserir veículo: {e}")
def atualizar_pessoa(self,pessoa):
    if self.conn:
        try:
            cursor = self.connn.cursor()
            cursor.execute(
                    "UPDATE Pessoa SET nome=?, nascimento=?,oculos=? WHERE cpf=?",
                    (pessoa.nome, pessoa.nascimento,pessoa.oculos,pessoa.cpf),
            )
            self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao atualizar pessoa: {e}")
def atualizar_veiculo(self, veiculo):
    if self.conn:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "UPDATE Veiculo SET cor=?, cpf_proprietario=?, id_marca=? WHERE placa=?",
                (
                    veiculo.cor,
                    veiculo.proprietario.cpf,
                    veiculo.marca.id,
                    veiculo.placa,
                ),
            )
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao atualizar veiculo: {e}")
with conexao:
    conexao.execute(f"""
        UPDATE pessoa
        SET{','.join(campos)}
        WHERE cpf =?;
        """,tuple(valores))

def apagar_veiculo(self, veiculo):
    if self.conn:
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM Veiculo WHERE placa=?",(veiculo.placa,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao apagar veiculo: {e}")

def buscar_todas_pessoas(self):
    pessoas = []
    if self.conn:
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT *FROM Pessoa")
            for row in cursor.fetchall():
                cpf,nome,nascimento,oculos = row
                pessoas.append(Pessoa(cpf,nome,nascimento,oculos))
        except sqlite3.Error as e:
            print(f"Erro ao buscar pessoas: {e}")
    return pessoas

def buscar_todos_veiculos(self):
    veiculos = []
    if self.conn:
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Veiculo")
            for row in cursor.fetchall():
                placa,cor,cpf_proprietario,id_marca = row
                proprietario = self.buscar_pessoa_por_cpf(cpf_proprietario)
                marca= self.buscar_marca_por_id(id_marca)
                veiculo.append(Veiculo(placa,cor,proprietario,marca))
        except sqlite3.Error as e:
            print(f"Erro ao buscar veículos: {e}")
    return veiculos

def buscar_pessoa_por_cpf(self, cpf: int):
    if self.conn:
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT *FROM Pessoa WHERE cpf=?", (cpf,))
            row = cursor.fetchone()
            if row:
                cpf, nome, nascimento, oculos = row
                return Pessoa(cpf, nome, nascimento, oculos)
        except sqlite3.Error as e:
            print(f"Erro ao buscar pessoa por CPF: {e}")
    return None
def fechar_conexao(self):
    if self.conn:
        self.conn.close()
        self.conn = None