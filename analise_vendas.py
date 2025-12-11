# ============================================================
#   PROJETO DE ANÁLISE DE DADOS - PORTFÓLIO PROFISSIONAL
#   Autor: SEU NOME
#   Objetivo: Analisar dados de vendas de forma completa
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------------
# 1. CONFIGURAÇÕES GERAIS (Estética, Janelas, Tabelas)
# ------------------------------------------------------------

# Forçar matplotlib a abrir em janela nativa
plt.switch_backend('tkagg')

# Ajustar a exibição de tabelas no terminal
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')

# Estilo dos gráficos
sns.set(style="whitegrid")

# ------------------------------------------------------------
# 2. CARREGAR O DATASET
# ------------------------------------------------------------

print("\n--- CARREGANDO DADOS ---\n")

df = pd.read_csv("vendas.csv")

print("Primeiras linhas:")
print(df.head(), "\n")

print("Informações gerais:")
print(df.info(), "\n")

print("Resumo estatístico:")
print(df.describe(), "\n")

# ------------------------------------------------------------
# 3. TRATAMENTO INICIAL
# ------------------------------------------------------------

print("\n--- TRATANDO DADOS ---\n")

# Converter datas
df["data"] = pd.to_datetime(df["data"], format="%Y-%m-%d")

# Ordenar dataset por data
df = df.sort_values("data")

# Criar coluna de mês
df["mes"] = df["data"].dt.strftime("%Y-%m")

# Verificar valores nulos
print("Valores nulos por coluna:")
print(df.isnull().sum(), "\n")

# ------------------------------------------------------------
# 4. ANÁLISES PRINCIPAIS
# ------------------------------------------------------------

print("\n--- ANÁLISES PRINCIPAIS ---\n")

# Total de vendas (R$)
total_vendas = df["valor_total"].sum()
print(f"Total geral vendido: R$ {total_vendas:,.2f}")

# Lucro total
lucro_total = df["lucro"].sum()
print(f"Lucro total: R$ {lucro_total:,.2f}")

# Quantidade total de itens vendidos
qtd_total = df["quantidade"].sum()
print(f"Quantidade total de itens vendidos: {qtd_total}")

# Vendas por categoria
print("\nVendas por categoria:")
print(df.groupby("categoria")["valor_total"].sum().sort_values(ascending=False))

# Lucro por categoria
print("\nLucro por categoria:")
print(df.groupby("categoria")["lucro"].sum().sort_values(ascending=False))

# Top 5 produtos mais vendidos
print("\nTop 5 produtos mais vendidos:")
print(df.groupby("produto")["quantidade"].sum().sort_values(ascending=False).head(5))

# Cidades que mais geram receita
print("\nFaturamento por cidade:")
print(df.groupby("cidade")["valor_total"].sum().sort_values(ascending=False))

# ------------------------------------------------------------
# 5. GRÁFICOS PROFISSIONAIS
# ------------------------------------------------------------

print("\n--- GERANDO GRÁFICOS ---\n")

# ----------------------------
# Gráfico 1: Faturamento por Categoria
# ----------------------------
plt.figure(figsize=(10, 5))
sns.barplot(
    data=df.groupby("categoria")["valor_total"].sum().reset_index(),
    x="categoria",
    y="valor_total"
)
plt.title("Faturamento por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Total em R$")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

# ----------------------------
# Gráfico 2: Faturamento por Cidade
# ----------------------------
plt.figure(figsize=(10, 5))
sns.barplot(
    data=df.groupby("cidade")["valor_total"].sum().reset_index(),
    x="cidade",
    y="valor_total"
)
plt.title("Faturamento por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Total em R$")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# ----------------------------
# Gráfico 3: Lucro por Mês
# ----------------------------
plt.figure(figsize=(10, 5))
sns.lineplot(
    data=df.groupby("mes")["lucro"].sum().reset_index(),
    x="mes",
    y="lucro",
    marker="o"
)
plt.title("Lucro por Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro total (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ----------------------------
# Gráfico 4: Produtos mais vendidos (Top 10)
# ----------------------------
top_produtos = (
    df.groupby("produto")["quantidade"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

plt.figure(figsize=(12, 5))
sns.barplot(data=top_produtos, x="produto", y="quantidade")
plt.title("TOP 10 Produtos Mais Vendidos")
plt.xlabel("Produto")
plt.ylabel("Quantidade")
plt.xticks(rotation=60)
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# 6. RELATÓRIO FINAL
# ------------------------------------------------------------

print("\n--- RELATÓRIO FINAL ---\n")

print(f"Faturamento total: R$ {total_vendas:,.2f}")
print(f"Lucro total: R$ {lucro_total:,.2f}")
print("\nCategorias mais lucrativas:")
print(df.groupby('categoria')['lucro'].sum().sort_values(ascending=False).head(3))

print("\nCidades mais rentáveis:")
print(df.groupby('cidade')['valor_total'].sum().sort_values(ascending=False).head(3))

print("\nVendedores de maior desempenho:")
print(df.groupby('vendedor')['valor_total'].sum().sort_values(ascending=False).head(5))

print("\nAnálise concluída com sucesso!")
