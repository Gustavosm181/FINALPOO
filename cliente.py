from produto import Produto
from utils import salvar_json, carregar_json
from typing import List

class Cliente:
    def __init__(self, nome: str, endereco: str):
        self._nome = nome
        self._endereco = endereco
        self._carrinho: List[Produto] = []

    def adicionar_ao_carrinho(self, produto, quantidade):
        if produto.estoque >= quantidade:
            self._carrinho.append((produto, quantidade))  # agora é uma tupla
            produto.estoque -= quantidade
        else:
            print("Produto em falta :(")


    def ver_carrinho(self):
        print(f"\nCarrinho de {self._nome}:")
        if not self._carrinho:
            print("Carrinho vazio.")
        for produto, quantidade in self._carrinho:
            print(f"{produto.nome} x {quantidade} = R${produto.preco * quantidade:.2f}")


    def finalizar_compra(self):
        total = sum(produto.preco * quantidade for produto, quantidade in self._carrinho)
        print(f"Pedido feito por {self._nome}, no endereço {self._endereco}.")
        print(f"Total: R$ {total:.2f}")
        self._carrinho.clear()


    def to_dict(self):
        return {"nome": self._nome, "endereco": self._endereco}
    
    @staticmethod
    def from_dict(data:dict):
        return Cliente(data['nome'], data['endereco'])
    

def salvar_cliente(cliente: Cliente, caminho: str = "cliente.json"):
    clientes = carregar_json(caminho)
    clientes.append(cliente.to_dict())
    salvar_json(caminho, clientes)