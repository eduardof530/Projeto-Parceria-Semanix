import pandas as pd
import numpy as np

def limpeza_preprocessamento():
    """
    Limpeza e preparação dos dados para análise de vendas e previsão de demanda.
    """
    df = pd.read_csv('BalajiFastFoodSales.csv')

    # Converter 'date' para datetime
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])

    # Colunas obrigatórias
    cols_essenciais = [
        'order_id', 'item_name', 'item_type', 'item_price',
        'quantity', 'transaction_amount', 'transaction_type',
        'received_by', 'time_of_sale'
    ]
    df = df.dropna(subset=cols_essenciais)

    # Tipos corretos
    df['order_id'] = df['order_id'].astype(str)
    df['item_name'] = df['item_name'].astype(str)
    df['item_type'] = df['item_type'].astype(str)
    df['transaction_type'] = df['transaction_type'].astype(str)
    df['received_by'] = df['received_by'].astype(str)
    df['time_of_sale'] = df['time_of_sale'].astype(str)
    df['quantity'] = df['quantity'].astype(int)
    df['item_price'] = df['item_price'].astype(float)
    df['transaction_amount'] = df['transaction_amount'].astype(float)

    # Remover valores inválidos
    df = df[(df['quantity'] > 0) & (df['item_price'] > 0) & (df['transaction_amount'] > 0)]

    # Verificar consistência de preço
    df['unit_price_calc'] = df['transaction_amount'] / df['quantity']
    diferenca = np.abs(df['unit_price_calc'] - df['item_price'])
    inconsistencias = diferenca > 0.01
    print(f"Inconsistências de preço detectadas: {inconsistencias.sum()}")
    df = df[~inconsistencias]

    # Arredondar valores monetários
    df['item_price'] = df['item_price'].round(2)
    df['transaction_amount'] = df['transaction_amount'].round(2)
    df['unit_price_calc'] = df['unit_price_calc'].round(2)

    # Criar colunas auxiliares
    df['weekday'] = df['date'].dt.day_name()
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year

    # Salvar dados limpos
    df.to_csv('BalajiFastFoodSales_limpo.csv', index=False)
    print("Arquivo limpo salvo como: BalajiFastFoodSales_limpo.csv")

    return df


def analise_descritiva(df):
    """
    Estatísticas descritivas para identificar padrões gerais.
    """
    print("\n=== Estatísticas Gerais ===")
    print(df[['quantity', 'item_price', 'transaction_amount']].describe())

    print("\n=== Top 10 Itens Mais Vendidos ===")
    top_itens = df.groupby('item_name')['quantity'].sum().sort_values(ascending=False).head(10)
    print(top_itens)

    print("\n=== Vendas por Tipo de Item ===")
    print(df.groupby('item_type')['quantity'].sum().sort_values(ascending=False))

    print("\n=== Média de Vendas por Dia da Semana ===")
    media_semana = df.groupby('weekday')['quantity'].mean().reindex([
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    print(media_semana)

    print("\n=== Vendas por Período do Dia ===")
    print(df.groupby('time_of_sale')['quantity'].sum())

    print("\n=== Vendas por Tipo de Transação ===")
    print(df.groupby('transaction_type')['quantity'].sum())

    print("\n=== Vendas Diárias (exemplo inicial) ===")
    print(df.groupby('date')['quantity'].sum().head(15))


def identificacao_variaveis(df):
    """
    Identificação de variáveis importantes e correlações.
    """
    print("\n=== Correlação entre Variáveis Numéricas ===")
    correlacao = df[['quantity', 'item_price', 'transaction_amount']].corr()
    print(correlacao)

    print("\n=== Quantidade por Tipo de Item ===")
    stats_tipo = df.groupby('item_type')['quantity'].describe()
    print(stats_tipo)

    print("\n=== Quantidade Média por Dia da Semana ===")
    media_dia = df.groupby('weekday')['quantity'].mean().reindex([
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    print(media_dia)

    print("\n=== Quantidade Média por Período do Dia ===")
    print(df.groupby('time_of_sale')['quantity'].mean())

    print("\n=== Quantidade Média por Tipo de Transação ===")
    print(df.groupby('transaction_type')['quantity'].mean())


def main():
    df = limpeza_preprocessamento()
    analise_descritiva(df)
    identificacao_variaveis(df)


if __name__ == "__main__":
    main()
