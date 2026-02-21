# Projeto 06 - Lista de Tarefas (To-Do List) ✅

!!! tip "Objetivo"
    **Objetivo**: Manipular Arrays (Vetores) para armazenamento temporário de dados e criar menus de navegação.

---

## O Desafio 🎯
Crie um gerenciador de tarefas simples via console. O sistema deve permitir que o usuário anote seus afazeres do dia e os visualize quando quiser.

## Requisitos Técnicos
1.  **Vetor**: Declare um vetor de String com 10 posições para guardar as tarefas.
2.  **Menu Interativo**: O programa deve exibir permanentemente (até que se escolha sair):
    *   `1. Adicionar Tarefa`
    *   `2. Listar Tarefas`
    *   `3. Sair`
3.  **Lógica de Inserção**: Ao adicionar, o sistema deve procurar a próxima "gaveta" vazia no vetor e guardar o texto lá.
4.  **Lógica de Listagem**: Ao listar, percorra o vetor e mostre apenas as posições que não estiverem em branco.

## Exemplo de Menu
```text
[1] Adicionar [2] Listar [3] Sair
Opção: 1
Digite a tarefa: Estudar Algoritmos

[1] Adicionar [2] Listar [3] Sair
Opção: 2
SUAS TAREFAS:
1. Estudar Algoritmos
--------------------
```

## Dica 💡
Use uma variável `contador` para saber quantas tarefas já foram adicionadas, assim você saberá exatamente em qual índice inserir a próxima.