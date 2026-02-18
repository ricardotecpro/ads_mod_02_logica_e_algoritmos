# Exercícios 12 - C# e .NET 🔷

> [!TIP]
> **Objetivo**: Produtividade e LINQ.

---

## 🟢 Fáceis

1.  **Console App**: Crie um programa que pergunte o nome do usuário e responda usando interpolação (`$"Olá {nome}"`).
2.  **Par ou Ímpar (Ternário)**: Leia um número. Use o operador ternário (`condicao ? verdadeiro : falso`) para exibir "Par" ou "Ímpar".

## 🟡 Médios

3.  **Lista de Frutas**: Crie uma `List<string>`. Adicione 5 frutas. Use um `foreach` para listar todas.
4.  **Filtro LINQ**:
    *   Crie uma lista de números: `1, 2, 3, 4, 5, 6, 7, 8, 9, 10`.
    *   Use LINQ (`.Where`) para criar uma nova lista apenas com os pares.
    *   Imprima a nova lista.

## 🔴 Desafio

5.  **Análise de Dados com LINQ**:
    *   Crie uma classe `Produto` (Nome, Preco, Categoria).
    *   Crie uma lista com 5 produtos variados.
    *   Use LINQ para encontrar:
        1.  O produto mais caro (`OrderByDescending` + `First`).
        2.  A média de preço de todos os produtos (`Average`).
