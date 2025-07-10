import json

class Produto:
    def __init__(self, nome, preco, estoque):
        self._nome = nome
        self._preco = preco
        self._estoque = estoque

    # Getters e Setters com encapsulamento
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str):
        if novo_nome:
            self._nome = novo_nome

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco: float):
        if novo_preco >= 0:
            self._preco = novo_preco

    @property
    def estoque(self):
        return self._estoque

    @estoque.setter
    def estoque(self, novo_estoque: int):
        if novo_estoque >= 0:
            self._estoque = novo_estoque

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f} (Estoque: {self.estoque})"

    def to_dict(self):
        return {
            "nome": self.nome,
            "preco": self.preco,
            "estoque": self.estoque
        }
    
    @staticmethod
    def from_dict(data: dict):
        return Produto(data['nome'], data['preco'], data['estoque'])

    def reduzir_estoque(self, quantidade: int) -> bool:
        if 0 < quantidade <= self._estoque:
            self._estoque -= quantidade
            return True
        return False
