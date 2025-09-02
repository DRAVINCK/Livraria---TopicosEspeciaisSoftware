from datetime import datetime
import random  # 8.11 Números aleatórios
from utils import formata_moeda, timestamp, eh_par, eh_impar  # 8.10 Módulos

# 8.1 Variaveis locais e globais
DESCONTO_PADRAO = 0.0117

#Entidade
"""
item = {nome, preco, quantidade}
"""

#Listas
itens = []
vendas = []

# 8.6 Funções como parâmetro
def imprime_lista(L, fimpressao, fcondicao):
    """Aplica fcondicao(e) e se True chama fimpressao(e) para cada elemento."""
    for e in L:
        if fcondicao(e):
            fimpressao(e)

def criterio_ordenacao_ranking(criterio_fn):
    """Recebe uma função (lambda) que retorna tupla de ordenação para o ranking."""
    return criterio_fn

# 8.7/8.8 Empacotamento e Desempacotamento de parâmetros
def cadastrar_item_em_lote(*itens_ou_dicts):
    adicionados = 0
    for dado in itens_ou_dicts:
        if isinstance(dado, dict):
            novo = {
                "nome": dado.get("nome"),
                "preco": float(dado.get("preco")),
                "quantidade": int(dado.get("quantidade"))
            }
            itens.append(novo)
            adicionados += 1
        elif isinstance(dado, tuple) and len(dado) == 3:
            nome, preco, quantidade = dado  # 8.8 Desempacotamento por tupla
            novo = {
                "nome": nome,
                "preco": float(preco),
                "quantidade": int(quantidade)
            }
            itens.append(novo)
            adicionados += 1
    print(f"\nItens adicionados em lote: {adicionados}")

def registrar_venda_kw(**dados):
    vendas_lista = dados["vendas"]
    venda = {
        "id": len(vendas_lista) + 1,
        "data": timestamp(),
        "item_nome": str(dados["item_nome"]),
        "preco_unitario": float(dados["preco_unitario"]),
        "quantidade": int(dados["quantidade"]),
        "valor_bruto": float(dados["valor_bruto"]),
        "desconto_aplicado": float(dados["valor_desconto"]),
        "valor_final": float(dados["valor_final"])
    }
    vendas_lista.append(venda)

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
        print(f"  Preço: {formata_moeda(item['preco'])}")
        print(f"  Estoque: {item['quantidade']} unidades")
        print("-" * 20)

# 8.5 Nomeando parâmetros p. 176
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

#8.3 Validação p. 173
def realizar_venda(itens, desconto):
    print("\n--- Realizar Venda ---")
    if not itens: # aqui validamos se a lista esta vazia
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

            # Desconto padrão se valor_bruto > 50
            if valor_bruto > 50.00:
                valor_desconto = valor_bruto * desconto

            # 8.11 Números aleatórios: desconto promocional extra aleatório (0% a 2%) se compra acima de 100
            desconto_extra_perc = random.uniform(0.0, 0.02) if valor_bruto > 100 else 0.0
            valor_desconto_extra = valor_bruto * desconto_extra_perc

            valor_final = valor_bruto - (valor_desconto + valor_desconto_extra)

            print("\n--- Resumo para Confirmação ---")
            print(f"Item: {item_selecionado['nome']} (x{quantidade_venda})")
            print(f"Valor Bruto: {formata_moeda(valor_bruto)}")
            if valor_desconto > 0:
                print(f"Desconto padrão ({desconto:.2%}): {formata_moeda(valor_desconto)}")
            if valor_desconto_extra > 0:
                print(f"Desconto promocional aleatório ({desconto_extra_perc:.2%}): {formata_moeda(valor_desconto_extra)}")
            print(f"Valor Final a Pagar: {formata_moeda(valor_final)}")

            confirmacao = input("\nConfirmar a venda? (S/N): ")

            if confirmacao.lower() == 's':
                item_selecionado["quantidade"] -= quantidade_venda

                # 8.8 Desempacotamento por **kwargs (usa registrar_venda_kw)
                venda_dict = {
                    "vendas": vendas,
                    "item_nome": item_selecionado["nome"],
                    "preco_unitario": item_selecionado["preco"],
                    "quantidade": quantidade_venda,
                    "valor_bruto": valor_bruto,
                    "valor_desconto": (valor_desconto + valor_desconto_extra),
                    "valor_final": valor_final
                }
                registrar_venda_kw(**venda_dict)

                # 8.11 Números aleatórios: sorteio de brinde simples
                if random.random() < 0.20:
                    print("Parabéns! Você ganhou um brinde 🎁")

                # 8.11: código promocional aleatório para próxima compra
                print(f"Código promocional para próxima compra: {gerar_codigo_promocional()}")

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

    total_liquido = calcular_faturamento(vendas)

    total_bruto = sum(v["valor_bruto"] for v in vendas)
    total_desconto = sum(v["desconto_aplicado"] for v in vendas)

    print(f"Quantidade de vendas: {len(vendas)}")
    print(f"Total Bruto: {formata_moeda(total_bruto)}")
    print(f"Total Descontos: {formata_moeda(total_desconto)}")
    print(f"Total Líquido: {formata_moeda(total_liquido)}")

    # 8.12 A função type: exibindo tipos de alguns campos
    exemplo = vendas[0]
    print("\n[Tipos de dados - 8.12]")
    print(f"type(id) = {type(exemplo['id'])}")
    print(f"type(data) = {type(exemplo['data'])}")
    print(f"type(preco_unitario) = {type(exemplo['preco_unitario'])}")
    print(f"type(valor_final) = {type(exemplo['valor_final'])}")

# 8.2 Funções recursivas
def calcular_faturamento(vendas_lista):
    if not vendas_lista:
        return 0
    return vendas_lista[0]["valor_final"] + calcular_faturamento(vendas_lista[1:])

# 8.4 Parâmetros opcionais
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
        # 8.9 Lambda para chave de ordenação
        ordenador = criterio_ordenacao_ranking(
            lambda par: (par[1]["quantidade"], par[1]["faturamento"])
        )
        ordenado = sorted(ranking.items(), key=ordenador, reverse=True)
        for nome, dados in ordenado:
            print(f" - {nome}: {dados['quantidade']} un. | Faturamento: {formata_moeda(dados['faturamento'])}")
    else:
        print("Nenhuma venda registrada para gerar ranking.")

    print("\nProdutos com baixo estoque:")
    # 8.6 + 8.9: usando função como parâmetro + lambda para condição e impressão
    imprime_lista(
        itens,
        fimpressao=lambda item: print(f" - {item['nome']}: {item['quantidade']} un."),
        fcondicao=lambda item: item["quantidade"] < limite_baixo_estoque
    )

# 8.11 Números aleatórios: gerador de código promocional
def gerar_codigo_promocional(tamanho=6, prefixo="PAP"):
    alfabeto = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    codigo = "".join(random.choices(alfabeto, k=tamanho))
    return f"{prefixo}-{codigo}"

# 8.12 A função type (extra): utilitário para mostrar tipos de um item
def mostrar_tipos_item(item):
    print("\n[Tipos do item - 8.12]")
    for k, v in item.items():
        print(f"{k}: {v} -> {type(v)}")

def main():
    print("--- Bem-vindo ao Sistema de Controle da Papelaria ---")

    # Exemplo opcional de 8.7 (cadastro em lote com *args) e 8.8 (desempacotamento por tuplas/dicts)
    # Descomente se quiser popular rapidamente:
    # cadastrar_item_em_lote(
    #     ("Caneta Azul", 3.5, 12),
    #     ("Caderno 10M", 18.9, 7),
    #     {"nome": "Borracha Branca", "preco": 2.0, "quantidade": 25}
    # )

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            cadastrar_item(itens)
        elif opcao == "2":
            listar_itens(itens)
            if itens:
                # 8.12: demonstrar tipos do primeiro item (opcional)
                mostrar_tipos_item(itens[0])
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
