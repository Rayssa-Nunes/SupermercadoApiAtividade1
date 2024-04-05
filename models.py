class Supermercado:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Produto(Supermercado):
    def __init__(self, id, nome):
        super().__init__(id, nome)

class Usuario(Supermercado):
    def __init__(self, id, nome):
        super().__init__(id, nome)

class Setor(Supermercado):
    def __init__(self, id, nome):
        super().__init__(id, nome)

class Categoria(Supermercado):
    def __init__(self, id, nome):
        super().__init__(id, nome)