from flask import request, jsonify, make_response
from src.Application.Service.user_service import user_service
from usuario_model import UsuarioModel

class UserController:
    @staticmethod
    def registrar_usuario():
        data = request.get_json()
        nome = data.get('nome')
        email = data.get('email')
        senha = data.get('senha')

        if not nome or not email or not senha:
            return make_response(jsonify({"erro": "Missing required fields"}), 400)

        usuario = UserService.criar_usuario(nome, email, senha)
        return make_response(jsonify({
            "mensagem": "Usuário salvo com sucesso",
            "usuarios": usuario.to_dict()
        }), 200)


class CadastroMercado (self):
    def __init__(self):
        self.CadastroMercado = [] #armazana os cadastros do mercado
        
        
    def adicionarMercado (self, nome, cnpj, email, celular, senha):  #essa função pega o cadastro do mercado e adicona em uma lista
        novo = Cadastro(nome , cnpj, email, celular, senha)
        self.CadastroMercado.append(novo)
        return novo
    
    
    def atualizar_perfil(self, cadastro, nome=None, cnpj=None, email=None, celular=None, senha=None, status=None):
        try:
            if nome: cadastro.nome = nome
            if cnpj: cadastro.cnpj = cnpj
            if email: cadastro.email = email
            if celular: cadastro.celular = celular
            if senha: 
                if len(senha) < 4:
                    raise ValueError("Senha muito curta!")
                self.__senha = senha
            if status: self.status = status
        except ValueError as senha:
            print(f"Erro ao atualizar perfil: {senha}")
    
    
    def cadastroAtivo(self):
        self.status = "Ativo"


    def cadastroInativo(self):
        self.status = "Inativo"


    def listarMercado(self):
        return CadastroMercado
    
    