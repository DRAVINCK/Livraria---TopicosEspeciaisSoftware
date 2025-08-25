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
def realizar_venda(itens, desconto):

    print("\n--- Realizar Venda ---")
    if not itens:
        print("Nenhum item cadastrado para vender.")
        return

    for i, item in enumerate(itens):
        print(f"[{i}] {item['nome']} - Estoque: {item['quantidade']}")

    try:
        indice_item = int(input("\nDigite o índice do item: "))
        quantidade_venda = int(input("Digite a quantidade: "))

        if 0 <= indice_item < len(itens):
            item_selecionado = itens[indice_item]

            if quantidade_venda > item_selecionado["quantidade"]:
                print(f"\nErro: Estoque insuficiente. Temos apenas {item_selecionado['quantidade']} unidades.")
                return

            valor_bruto = item_selecionado["preco"] * quantidade_venda
            valor_desconto = 0

            if valor_bruto > 50.00:
                valor_desconto = valor_bruto * desconto

            valor_final = valor_bruto - valor_desconto

            print("\n--- Resumo para Confirmação ---")
            print(f"Item: {item_selecionado['nome']} (x{quantidade_venda})")
            print(f"Valor Bruto: R$ {valor_bruto:.2f}")
            if valor_desconto > 0:
                print(f"Desconto ({desconto:.2%}): R$ {valor_desconto:.2f}")
            print(f"Valor Final a Pagar: R$ {valor_final:.2f}")

            confirmacao = input("\nConfirmar a venda? (S/N): ")

            if confirmacao.lower() == 's':

                item_selecionado["quantidade"] -= quantidade_venda

                print("\n--- Venda Realizada com Sucesso! ---")
                print(f"Estoque restante de '{item_selecionado['nome']}': {item_selecionado['quantidade']} unidades.")
            else:
                print("\n--- Venda cancelada pelo usuário. ---")

        else:
            print("\nErro: Índice de item inválido.")
    except ValueError:
        print("\nErro: Índice e quantidade devem ser números inteiros.")

# define a logica de main para navegar entre os metodos
def main():

    print("--- Bem-vindo ao Sistema de Controle da Papelaria ---")

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            cadastrar_item(itens)
        elif opcao == "2":
            listar_itens(itens)
        elif opcao == "3":
            realizar_venda(itens, DESCONTO_PADRAO)
        elif opcao == "4":
            print("\nSaindo do sistema... Até logo!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha um número de 1 a 4.")
            
if __name__ == "__main__":
    main()
