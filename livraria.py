from datetime import datetime

# 8.1 Variaveis locais e globais
DESCONTO_PADRAO = 0.0117

#Entidade
"""
item = {nome, preco, quantidade}
"""

#Listas
itens = []
vendas = []

#metodos

def exibir_menu():
    print("\n--- Menu da Papelaria ---")
    print("1. Cadastrar novo item")
    print("2. Listar todos os itens")
    print("3. Realizar venda")
    print("4. Relatórios")
    print("5. Sair")
    return input("Escolha uma opção: ")

def exibir_menu_relatorios():
    print("\n--- Relatórios ---")
    print("1. Totais gerais")
    print("2. Produtos (ranking e baixo estoque)")
    print("0. Voltar")
    return input("Escolha uma opção: ")

def cadastrar_item(itens):
    print("\n--- Cadastro de Novo Item ---")
    nome = input("Digite o nome do item (ex: Caneta Azul): ")

    try:
        preco = float(input("Digite o preço: ").replace(",", ".").replace(" ", ""))
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

def registrar_venda(vendas, item_nome, preco_unitario, quantidade, valor_bruto, valor_desconto, valor_final):
    venda = {
        "id": len(vendas) + 1,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "item_nome": item_nome,
        "preco_unitario": float(preco_unitario),
        "quantidade": int(quantidade),
        "valor_bruto": float(valor_bruto),
        "desconto_aplicado": float(valor_desconto),
        "valor_final": float(valor_final)
    }
    vendas.append(venda)

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
                registrar_venda(
                    vendas=vendas,
                    item_nome=item_selecionado["nome"],
                    preco_unitario=item_selecionado["preco"],
                    quantidade=quantidade_venda,
                    valor_bruto=valor_bruto,
                    valor_desconto=valor_desconto,
                    valor_final=valor_final
                )
                print("\n--- Venda Realizada com Sucesso! ---")
                print(f"Estoque restante de '{item_selecionado['nome']}': {item_selecionado['quantidade']} unidades.")
            else:
                print("\n--- Venda cancelada pelo usuário. ---")

        else:
            print("\nErro: Índice de item inválido.")
    except ValueError:
        print("\nErro: Índice e quantidade devem ser números inteiros.")

def relatorio_totais_gerais(vendas):
    print("\n--- Relatório: Totais Gerais ---")
    if not vendas:
        print("Nenhuma venda registrada.")
        return

    total_bruto = sum(v["valor_bruto"] for v in vendas)
    total_desconto = sum(v["desconto_aplicado"] for v in vendas)
    total_liquido = sum(v["valor_final"] for v in vendas)
    qtde_vendas = len(vendas)

    print(f"Quantidade de vendas: {qtde_vendas}")
    print(f"Total Bruto: R$ {total_bruto:.2f}")
    print(f"Total Descontos: R$ {total_desconto:.2f}")
    print(f"Total Líquido: R$ {total_liquido:.2f}")

def relatorio_produtos(itens, vendas, limite_baixo_estoque=5):
    print("\n--- Relatório: Produtos ---")
    ranking = {}
    for v in vendas:
        nome = v["item_nome"]
        ranking.setdefault(nome, {"quantidade": 0, "faturamento": 0.0})
        ranking[nome]["quantidade"] += v["quantidade"]
        ranking[nome]["faturamento"] += v["valor_final"]

    if ranking:
        print("\nTop produtos vendidos:")
        ordenado = sorted(ranking.items(), key=lambda kv: (kv[1]["quantidade"], kv[1]["faturamento"]), reverse=True)
        for nome, dados in ordenado:
            print(f" - {nome}: {dados['quantidade']} un. | Faturamento: R$ {dados['faturamento']:.2f}")
    else:
        print("Nenhuma venda registrada para gerar ranking.")

    print("\nProdutos com baixo estoque:")
    baixo = [item for item in itens if item["quantidade"] < limite_baixo_estoque]
    if baixo:
        for item in baixo:
            print(f" - {item['nome']}: {item['quantidade']} un.")
    else:
        print("Nenhum produto com baixo estoque.")

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
            while True:
                op_r = exibir_menu_relatorios()
                if op_r == "1":
                    relatorio_totais_gerais(vendas)
                elif op_r == "2":
                    relatorio_produtos(itens, vendas)
                elif op_r == "0":
                    break
                else:
                    print("Opção inválida de relatório.")
        elif opcao == "5":
            print("\nSaindo do sistema... Até logo!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha um número de 1 a 5.")

if __name__ == "__main__":
    main()
