# Constante
DESCONTO_PADRAO = 0.0117

#Entidade
"""
item = {nome, preco, quantidade}
"""

#Listas
itens = []

#metodos

#fazer metodo de exibir o menu
def exibir_menu():
    print("\n--- Menu da Papelaria ---")
    print("1. Cadastrar novo item")
    print("2. Listar todos os itens")
    print("3. Realizar venda")
    print("4. Sair")
    return input("Escolha uma opção: ")


# fazer o metodo para cadastrar item
def cadastrar_item(itens):
    print("\n--- Cadastro de Novo Item ---")
    nome = input("Digite o nome do item (ex: Caneta Azul): ").replace(",", ".").replace(" ", "")

    try:
        preco = float(input("Digite o preço: "))
        quantidade = int(input("Digite a quantidade em estoque: ").replace(" ", ""))
    except ValueError:
        print("\nErro: Preço e quantidade precisam ser números. Operação cancelada.")
        return

    novo_item = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    itens.append(novo_item)
    print(f"\nItem '{nome}' cadastrado com sucesso!")

# fazer o metodo para listar os itens
def listar_itens(itens):

    print("\n--- Lista de Itens Cadastrados ---")
    if not itens:
        print("Nenhum item cadastrado ainda.")
        return

    for i, item in enumerate(itens):
        print(f"Indice: {i}")
        print(f"  Nome: {item['nome']}")
        print(f"  Preço: R$ {item['preco']:.2f}")
        print(f"  Estoque: {item['quantidade']} unidades")
        print("-" * 20)

#fazer metodo de realizar venda


# define a logica de main para navegar entre os metodos -- fazer por ultimo


"""if __name__ == "__main__":
    main()""""
