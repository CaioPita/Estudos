from produto import Produto

def main():
    produtos = []

    while True:
        print("\nMenu:")
        print("1 - Adicionar Produto")
        print("2 - Atualizar Preço")
        print("3 - Atualizar Quantidade")
        print("4 - Listar Produtos")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade do produto: "))
            produto = Produto(nome, preco, quantidade)
            produtos.append(produto)
            print(f"{nome} adicionado com sucesso!")
        elif opcao == '2':
            nome = input("Nome do produto para atualizar o preço: ")
            for produto in produtos:
                if produto.nome == nome:
                    novo_preco = float(input("Novo preço: R$ "))
                    produto.atualizar_preco(novo_preco)  # Atualiza o preço do produto
                    print(f"Preço de {nome} atualizado para R${novo_preco:.2f}.")
                    break
            else:
                print("Produto não encontrado.")
        elif opcao == '3':
            nome = input("Nome do produto para atualizar a quantidade: ")
            for produto in produtos:
                if produto.nome == nome:
                    nova_quantidade = int(input("Nova quantidade: "))
                    produto.atualizar_quantidade(nova_quantidade)  # Atualiza a quantidade do produto
                    print(f"Quantidade de {nome} atualizada para {nova_quantidade}.")
                    break
            else:
                print("Produto não encontrado.")
        elif opcao == '4':
            if produtos:
                print("\nLista de Produtos: ")
                for produto in produtos:
                    print(f"Nome: {produto.nome}, Preço: R${produto.preco:.2f}, Quantidade: {produto.quantidade}")
            else:
                print("Nenhum produto cadastrado.")
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
