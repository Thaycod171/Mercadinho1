from src.Domain.user import UserDomain
from src.Infrastructure.Model.user import User
from src.config.data_base import db 

class UserService:
    @staticmethod
    def criar_usuario(nome, email, senha):
        novo_usuario = UserDomain(nome, email, senha)
        usuario = User(nome=novo_usuario.nome, email=novo_usuario.email, senha=novo_usuario.senha)        
        db.session.add(usuario)
        db.session.commit()
        return usuario
