# Projeto 13 - Analisador de Dados CSV 🐍

!!! tip "Objetivo"
    **Objetivo**: Manipular arquivos externos, processar coleções de dados (Listas e Dicionários) e realizar cálculos básicos de estatística com Python.

---

## O Desafio 🎯
Você recebeu um arquivo `vendas.csv` com centenas de linhas contendo: `Produto, Preço, Quantidade`. Sua missão é criar um script que automatize a geração de um relatório de desempenho.

## Requisitos Técnicos
1.  **Leitura de Arquivo**: Use as funções nativas do Python (`open`, `readlines`) para ler o arquivo sem bibliotecas externas.
2.  **Estrutura de Dados**: Converta cada linha do CSV em um **Dicionário** para facilitar o acesso.
3.  **Processamento**:
    *   Calcule o **Faturamento Total** (Preço * Quantidade).
    *   Identifique qual foi o **Produto mais vendido** em quantidade.
4.  **Saída**: Grave os resultados em um novo arquivo chamado `resumo_vendas.txt`.

## Exemplo de entrada (vendas.csv)
```csv
Teclado, 150.00, 10
Mouse, 80.00, 25
Monitor, 1200.00, 2
```

## Por que não usar Pandas? 🤔
O objetivo deste projeto é entender como o Python lida com strings e arquivos "sob o capô" antes de usar ferramentas automáticas. Isso fortalece sua lógica de manipulação de strings!