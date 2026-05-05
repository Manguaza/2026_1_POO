#from cliente import Cliente, ClienteDAO
#from categoria import Categoria, CategoriaDAO
from views import View

class UI:
    usuario = None   # atributos de classe
    admin = False

    @classmethod
    def main(cls):
        op = 0
        while op != 9:
            op = UI.menu_visitante()
            if op == 1: UI.entrar_no_sistema()
            #if op == 2: UI.criar_conta()
            if cls.usuario != None: print("Bem-vindo(a),", cls.usuario.nome)  
            op = 0
            if cls.admin:  
                while op != 9:
                    op = UI.menu_admin()
                    if op == 1: UI.cliente_inserir()
                    if op == 2: UI.cliente_listar()
                    if op == 3: UI.cliente_atualizar()
                    if op == 4: UI.cliente_excluir()
                    if op == 5: UI.categoria_inserir()
                    if op == 6: UI.categoria_listar()

    @staticmethod
    def menu_visitante():
        print("1-Entrar no sistema 2-Criar conta 9-Fim")
        return int(input("Informe uma opção: "))

    @classmethod
    def entrar_no_sistema(cls):
        email = input("Informe o e-mail: ")
        senha = input("Informe a senha: ")
        cls.usuario = View.cliente_validar(email, senha)
        if cls.usuario == None:
            print("E-mail ou senha inválido(s)")
        else:
            admin = cls.usuario.email == "admin"    

    @staticmethod
    def menu_admin():
        print("----- Clientes -----")
        print("1-Inserir 2-Listar 3-Atualizar 4-Excluir")
        print("----- Categorias -----")
        print("5-Inserir 6-Listar 7-Atualizar 8-Excluir")
        print("9-Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def cliente_inserir():                           # C - Create
        print("Cadastro de Clientes")
        #id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        senha = input("Informe a senha: ")
        #c = Cliente(0, nome, email, fone)
        #ClienteDAO().inserir(c)
        View.cliente_inserir(nome, email, fone, senha)

    @staticmethod
    def cliente_listar():                            # R - Read
        print("Listagem de Clientes")
        #for c in ClienteDAO().listar(): print(c)
        for c in View.cliente_listar(): print(c)

    def cliente_atualizar():                         # U - Update
        UI.cliente_listar()
        id = int(input("Qual o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")
        senha = input("Informe a nova senha: ")
        #c = Cliente(id, nome, email, fone)
        #ClienteDAO().atualizar(c)
        View.cliente_atualizar(id, nome, email, fone, senha)
    def cliente_excluir():                           # D - Delete
        UI.cliente_listar()
        id = int(input("Qual o id do cliente a ser excluído: "))
        #c = Cliente(id, "", "", "")
        #ClienteDAO().excluir(c)
        View.cliente_excluir(id)

    @staticmethod
    def categoria_inserir():                           # C - Create
        print("Cadastro de Categorias")
        desc = input("Informe a descrição: ")
        #c = Categoria(0, desc)
        #CategoriaDAO().inserir(c)
        View.categoria_inserir(desc)

    @staticmethod
    def categoria_listar():                            # R - Read
        print("Listagem de Categorias")
        #for c in CategoriaDAO().listar(): print(c)
        for c in View.categoria_listar(): print(c)

UI.main()
