import json
from typing import List #que import é esse
from produto import Produto
from utils import salvar_json, carregar_json
class Dono:
    def __init__(self, caminho_arquivo: str = "produtos.json"):
        self.caminho = caminho_arquivo
        self.produtos: List[Produto] = self.carregar_produtos()

    def adicionar_produto(self, nome: str, preco: float, estoque: int):
        novo_produto = Produto(nome, preco, estoque)
        self.produtos.append(novo_produto)  
        self.salvar_produto()

    def listar_produtos(self):
        for i, produto in enumerate(self.produtos):
            print(f"{i + 1}. {produto}")
    
    def pegar_produto(self, index:int) -> Produto: 
        return self.produtos[index]
    
    def salvar_produto(self):
        salvar_json(self.caminho, [p.to_dict() for p in self.produtos])

    def carregar_produtos(self) -> list[Produto]: # oq é essa seta
        dados = carregar_json(self.caminho)
        return [Produto.from_dict(p) for p in dados]
