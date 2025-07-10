from cliente import Cliente, salvar_cliente
from dono import Dono

def menu():
    print("\n1. Adicionar produto (dono)")
    print("2. Listar produtos")
    print("3. Criar cliente")
    print("4. Adicionar produto ao carrinho")
    print("5. Ver carrinho")
    print("6. Finalizar compra")
    print("0. Sair")

def main():
    dono = Dono()
    cliente = None

    while True:
        menu()
        op = input("Escolha uma opcao: ")

        if op == '1':
            nome = input("Nome do produto: ")
            preco = float(input("Preço: "))
            estoque = int(input("Quantidade em estoque: "))
            dono.adicionar_produto(nome, preco, estoque)

        elif op == '2':
            dono.listar_produtos()

        elif op == '3':
            nome = input("Nome do cliente: ")
            endereco = input("Endereço: ")
            cliente = Cliente(nome, endereco)
            salvar_cliente(cliente)

        elif op == '4':
            if not cliente:
                print("Crie um cliente primeiro.")
                continue
            dono.listar_produtos()
            idx = int(input("Escolha o número do produto: ")) - 1
            produto = dono.pegar_produto(idx)

            if produto:
                quantidade = int(input("Quantidade desejada: "))
                cliente.adicionar_ao_carrinho(produto, quantidade)
                dono.salvar_produto()
            else:
                print("Produto inválido.")

        elif op == '5':
            if cliente:
                cliente.ver_carrinho()
            else:
                print("Nenhum cliente criado.")

        elif op == '6':
            if cliente:
                cliente.finalizar_compra()
            else:
                print("Nenhum cliente criado.")

        elif op == '0':
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
