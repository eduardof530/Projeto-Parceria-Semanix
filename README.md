# 📊 Análise de Vendas em Restaurante Fast Food

## 🎯 Objetivo do Projeto

Analisar dados de vendas de um restaurante fast food com o objetivo de identificar padrões de consumo, horários de pico, itens mais vendidos e fatores que afetam a demanda, visando otimizar estoque, produção e atendimento ao cliente.

Dissertação sobre o Problema

📌 Descrição do Problema
    Restaurantes enfrentam o desafio constante de prever corretamente a demanda diária por alimentos e bebidas. Quando a previsão é incorreta, podem ocorrer dois problemas principais: o desperdício de alimentos perecíveis quando a demanda é menor do que o esperado, e a falta de produtos ou demora no atendimento quando a demanda é maior. Ambos os cenários geram prejuízos financeiros, impactam a experiência do cliente e comprometem a sustentabilidade do negócio.

📌 Importância e relevância do problema
    Esse problema é especialmente relevante em pequenas e médias empresas do setor alimentício, que têm menos margem de erro e recursos para absorver perdas. Em um contexto de aumento nos custos de insumos, exigências sanitárias rigorosas e competitividade alta, gerenciar corretamente o estoque e a produção é fundamental para a sobrevivência do negócio. Além disso, a redução do desperdício de alimentos também contribui para práticas mais sustentáveis e alinhadas aos Objetivos de Desenvolvimento Sustentável (ODS), como o combate à fome e à redução de resíduos.

📌 Como a análise de dados pode ajudar a solucionar o problema
    A análise de dados permite identificar padrões de consumo com base em variáveis como o dia da semana, clima, datas comemorativas, eventos locais, promoções e até o histórico de vendas. Com essas informações, é possível criar modelos de previsão mais precisos, ajudando na tomada de decisão sobre o que, quanto e quando preparar cada item do cardápio. Ferramentas como séries temporais, regressão e machine learning podem ser aplicadas para melhorar a acurácia das previsões, otimizando o planejamento da produção e do estoque.

- Coleta de dados

Dataset principal: Restaurant Sales report
- Origem: Kaggle
- Autor: rajatsurana979
- Link: https://www.kaggle.com/datasets/rajatsurana979/fast-food-sales-report
- Formato: CSV
- Tipo de dados: Estruturados (tabela com colunas)
- Acesso: Download direto após login no Kaggle

## 💡  Relatório de Insights

## 💡 Relatório de Insights

### 1. Estatísticas Gerais

| Métrica                | Quantidade | Preço Unitário (R$) | Valor Total da Transação (R$) |
|------------------------|------------|----------------------|-------------------------------|
| Média                  | 8,02       | 34,29                | 277,68                        |
| Desvio padrão          | 4,41       | 15,32                | 210,76                        |
| Intervalo interquartil | 4 – 12     | 20 – 50              | 120 – 375                     |
| Máximo observado       | 15         | 60                   | 900                           |

✅ **Conclusão**: As vendas por transação são relativamente altas, sugerindo pedidos grandes ou múltiplos itens por vez — isso pode ajudar na previsão de insumos.

---

### 2. Itens Mais Vendidos

Top produtos por volume:

- Cold coffee (465)
- Frankie (463)
- Sandwich, Sugarcane juice, Vadapav

✅ **Conclusão**: Produtos do tipo *Fastfood* dominam o ranking — são os principais alvos para prever demanda.

---

### 3. Tipo de Item Vendido

- **Fastfood**: 2.036 unidades  
- **Beverages**: 890 unidades  

✅ **Conclusão**: Fastfood representa mais de 69% das vendas — prioridade máxima em planejamento e controle de estoque.

---

### 4. Padrão por Dia da Semana

- **Terça-feira** tem a maior média de vendas (9,06 unidades por transação).
- **Sábado** tem a menor (7,09).

✅ **Conclusão**: A demanda não é necessariamente maior nos fins de semana. Pode haver comportamento local que justifique maior consumo em dias úteis (ex: ponto comercial em região corporativa?).

---

### 5. Vendas por Período do Dia

- **Night**: 8,79 unidades por venda  
- **Midnight** e **Morning** também têm alta média  
- **Afternoon** tem a menor média  

✅ **Conclusão**: Alta demanda no turno da noite e madrugada — planejamento de equipe e estoque deve focar nesses períodos.

---

### 6. Transações por Tipo

- **Cash**: 1.630 unidades  
- **Online**: 1.296 unidades  

✅ **Conclusão**: Vendas em dinheiro ainda são predominantes, mas o online também é relevante e deve ser monitorado separadamente para comportamento de compra.

---

### 7. Correlação entre Variáveis

| Variáveis              | Correlação |
|------------------------|------------|
| Quantity x Amount      | 0.74       |
| Item Price x Amount    | 0.61       |
| Quantity x Item Price  | 0.04       |

✅ **Conclusão**:
- O volume de itens vendidos (**quantity**) tem forte relação com o valor da venda total.
- O preço unitário por si só tem influência, mas bem menor na variação do valor total.

---

## 📌 Recomendações com Base nos Dados

1. Prever demanda com foco em **dias úteis** e **turnos noturnos**, especialmente para produtos fast food.
2. Dar atenção especial às **terças, quintas e noites**, onde a média de vendas é mais alta.
3. Separar o planejamento de **bebidas**, pois representam uma fatia menor, mas podem ter padrões próprios (ex: clima quente = mais vendas).
4. Explorar diferenciação entre **pagamentos online e cash**, que podem ter perfis de clientes e horários diferentes.
5. Usar esses padrões para alimentar **modelos preditivos simples** (ex: regressão linear com dia da semana e hora).

---

### 🛠️ Sugestões de Ações

1. Reforçar produção e equipe em dias e turnos de maior demanda.
2. Estocar mais os itens mais vendidos e usar em promoções.
3. Incentivar pagamentos online com promoções.
4. Monitorar consistência de preços para evitar erros.
5. Reduzir desperdício com modelos de previsão simples.

---

## 📊 Dashboard no Looker Studio

- Visualizações interativas com dados filtráveis por período, tipo e forma de pagamento
- Gráficos utilizados:
  - Top 10 itens mais vendidos
  - Vendas por tipo de item
  - Média de vendas por dia da semana
  - Média de vendas por período do dia
  - Distribuição por forma de pagamento
  - Evolução temporal das vendas (linha do tempo)
  - Insights e sugestões

---

🔗 ** LINK PARA O DASHBOARD LOOKER STUDIO **: https://lookerstudio.google.com/reporting/ee6cf25e-c303-4c63-a524-14ef90450e12

---

## 📁 Arquivos do Projeto

| Arquivo | Descrição |
|--------|-----------|
| `BalajiFastFoodSales.csv` | Arquivo original baixado do Kaggle |
| `BalajiFastFoodSales_limpo.csv` | Versão limpa e formatada para análise |
| `README.md` | Documentação completa do projeto |

---

## 🧾 Conclusão

Este projeto mostra como a análise de dados pode resolver problemas reais no setor de alimentação, apoiando decisões estratégicas e operacionais por meio de insights claros e acionáveis.

---

## 🚀 Desenvolvido por

Eduardo Farias |
