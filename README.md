# Sistema de Controle da Papelaria — README

Aplicação de console em Python para **controle básico de uma papelaria**: cadastro e listagem de itens, realização de vendas com **desconto padrão** e **relatórios** (totais e produtos). Tudo em **memória** (listas Python), sem dependências externas.

---

## ✨ Funcionalidades

* **Cadastrar múltiplos produtos** (`nome`, `preco`, `quantidade`).
* **Listar** produtos com preço formatado e estoque.
* **Realizar venda** de um item por vez:

  * Bloqueia se a **quantidade** desejada for maior que o **estoque**.
  * Calcula **valor bruto**.
  * Aplica **desconto** `DESCONTO_PADRAO` **apenas se** `valor_bruto > 50.00`.
  * Atualiza estoque com operador `-=`.
  * **Registra a venda** em `vendas`.
* **Relatórios**:

  * **Totais gerais**: quantidade de vendas, somatórios de **bruto**, **descontos** e **líquido**.
  * **Produtos**: ranking por quantidade/faturamento e **baixo estoque** (padrão `< 5`).

---

## 🧰 Requisitos

* **Python 3.8+**
* Sem bibliotecas externas.

---

## 📁 Estrutura (em memória)

* **Constante**

  * `DESCONTO_PADRAO = 0.0117` (1,17%)
* **Entidade (dicionário)**

  * `item = { "nome": str, "preco": float, "quantidade": int }`
* **Listas**

  * `itens: list[dict]` — catálogo de produtos
  * `vendas: list[dict]` — histórico de vendas (uma venda = um item vendido)

> Cada venda registrada possui: `id`, `data`, `item_nome`, `preco_unitario`, `quantidade`, `valor_bruto`, `desconto_aplicado`, `valor_final`.

---

## ▶️ Como executar

Salve o código como `app.py` e rode:

```bash
python app.py
```

---

## 🧭 Fluxo pelo menu

**Menu principal**

```
1. Cadastrar novo item
2. Listar todos os itens
3. Realizar venda
4. Relatórios
5. Sair
```

**Relatórios**

```
1. Totais gerais
2. Produtos (ranking e baixo estoque)
0. Voltar
```

---

## 🧪 Regras e validações implementadas

* **Conversões e tipos**

  * `preco` → `float`
  * `quantidade` → `int`
  * Mensagens claras em caso de `ValueError`.
* **Listagem**

  * Verifica se há itens cadastrados antes de listar.
* **Venda**

  * Bloqueia se `quantidade_venda > estoque`.
  * **Desconto** aplicado apenas quando `valor_bruto > 50.00`:

    * `valor_desconto = valor_bruto * DESCONTO_PADRAO`
    * `valor_final = valor_bruto - valor_desconto`
  * Estoque atualizado com `item["quantidade"] -= quantidade_venda`.
  * Venda **registrada** em `vendas`.
* **Formatação**

  * Valores monetários com duas casas decimais (`:.2f`).

---

## 🧾 Exemplos rápidos (interação)

**Cadastro**

```
1 (Cadastrar novo item)
Nome: CanetaAzul
Preço: 2.50
Quantidade: 100
```

**Venda**

```
3 (Realizar venda)
[0] CanetaAzul - Estoque: 100
Índice: 0
Quantidade: 30
Valor Bruto: R$ 75.00
Desconto (1.17%): R$ 0.88
Valor Final a Pagar: R$ 74.12
→ Estoque restante: 70
```

**Relatórios**

```
4 (Relatórios)
1 (Totais gerais)
Quantidade de vendas: 1
Total Bruto: R$ 75.00
Total Descontos: R$ 0.88
Total Líquido: R$ 74.12

4 (Relatórios)
2 (Produtos)
Top produtos vendidos:
 - CanetaAzul: 30 un. | Faturamento: R$ 74.12

Produtos com baixo estoque:
Nenhum produto com baixo estoque.
```

---

## 🧱 Limitações atuais

* Persistência **somente em memória** (dados se perdem ao encerrar).
* Venda **de um item por vez** (não há carrinho multi-itens).
* `DESCONTO_PADRAO` é fixo no código (não há ajuste via menu).

---

## 🚀 Próximos passos sugeridos

* Persistir `itens` e `vendas` em **JSON** ou **SQLite**.
* Suportar **carrinho** (múltiplos itens por venda).
* Parametrizar o **limite de baixo estoque** no menu.
* Ajustar normalização de `nome` (atualmente remove espaços).

---

## 📜 Licença

Uso educacional/acadêmico. Adapte conforme sua necessidade.
