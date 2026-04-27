from cliente import Cliente, ClienteDAO
from categoria import Categoria, CategoriaDAO

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            if op == 5: UI.categoria_inserir()
            if op == 6: UI.categoria_listar()
    @staticmethod
    def menu():
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
        c = Cliente(0, nome, email, fone)
        ClienteDAO().inserir(c)
    @staticmethod
    def cliente_listar():                            # R - Read
        print("Listagem de Clientes")
        for c in ClienteDAO().listar(): print(c)
    def cliente_atualizar():                         # U - Update
        UI.listar()
        id = int(input("Qual o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")
        c = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(c)
    def cliente_excluir():                           # D - Delete
        UI.listar()
        id = int(input("Qual o id do cliente a ser excluído: "))
        c = Cliente(id, "", "", "")
        ClienteDAO().excluir(c)

    @staticmethod
    def categoria_inserir():                           # C - Create
        print("Cadastro de Categorias")
        desc = input("Informe a descrição: ")
        c = Categoria(0, desc)
        CategoriaDAO().inserir(c)
    @staticmethod
    def categoria_listar():                            # R - Read
        print("Listagem de Categorias")
        for c in CategoriaDAO().listar(): print(c)


UI.main()
