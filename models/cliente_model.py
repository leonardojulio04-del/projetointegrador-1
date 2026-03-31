#Model usuario
from models.conexao import *
class Cliente(Base):
    __tablename__ = "clientes"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(200))
    telefone = Column("telefone", String(15))
    #A funçao __init__ serve para inicializar a classe (construtor da classe)


Base.metadata.create_all(bind=engine)