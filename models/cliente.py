from conection.conexao import db
from sqlalchemy.sql import func


class Cadastrocliente(db.Model):
    __tablename__ = 'cadastro_cliente'
    __table_args__ = {"extend_existing": True}
    id = db.Column('id', db.Integer, primary_key=True)
    nome = db.Column('nome', db.String())
    razao_social = db.Column('razao_social', db.String())
    cnpj_cpf = db.Column('cnpj_cpf', db.String())
    cidade = db.Column('cidade', db.String())
    UF = db.Column('UF', db.String())
    email = db.Column('email', db.String())
    telefone = db.Column('telefone', db.String())
    data_cadastro = db.Column('data_cadastro', db.DateTime, default=func.now())
    
    
    def __init__(self, nome, razao_social, cnpj_cpf, cidade, UF, email, telefone):
        self.nome = nome
        self.razao_social = razao_social
        self.cnpj_cpf = cnpj_cpf
        self.cidade = cidade
        self.UF = UF
        self.email = email
        self.telefone = telefone
        

