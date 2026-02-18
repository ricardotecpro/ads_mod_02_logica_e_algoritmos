# Exercícios 16 - PHP e Web 🐘

!!! tip "Objetivo"
    **Objetivo**: Backend e Dados.

---

## 🟢 Fáceis

1.  **Data e Hora**: Crie um script PHP que mostre: "Hoje é dia [d/m/Y] e são [H:i] horas".
2.  **Array Associativo**: Crie um array `$pessoa` com nome e idade. Mostre com `echo`.

## 🟡 Médios

3.  **Formulário Simples**:
    *   Crie um HTML com campo "nome" e botão "Enviar".
    *   No PHP, verifique se o nome foi enviado (`isset($_GET['nome'])`).
    *   Se sim, mostre "Olá [nome]". Se não, mostre "Digite seu nome".
4.  **Loop HTML**:
    *   Crie um array com 5 nomes de cidades.
    *   Use `foreach` para gerar uma lista `<ul><li>` com essas cidades no HTML.

## 🔴 Desafio

5.  **Simulador de Banco de Dados**:
    *   Crie uma classe `Conexao`.
    *   Método `conectar()`: Retorna "Conectado ao MySQL".
    *   Método `buscar(id)`: Retorna "Buscando usuário ID...".
    *   Simule o processo de buscar um usuário e mostrar na tela.