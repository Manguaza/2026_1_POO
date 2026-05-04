# View acessa as classes do Modelo
from cliente import Cliente, ClienteDAO
from categoria import Categoria, CategoriaDAO

class View: # nenhum print, nenhum input
    @staticmethod
    def cliente_inserir(nome, email, fone):
        c = Cliente(0, nome, email, fone)
        ClienteDAO().inserir(c)

    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        c = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(c)

    @staticmethod
    def cliente_excluir(id):
        c = Cliente(id, "", "", "")
        ClienteDAO().excluir(c)

    @staticmethod
    def categoria_inserir(desc):
        c = Categoria(0, desc)
        CategoriaDAO().inserir(c)

    @staticmethod
    def categoria_listar():
        return CategoriaDAO().listar()
