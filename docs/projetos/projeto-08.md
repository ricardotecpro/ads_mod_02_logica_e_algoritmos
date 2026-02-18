# Projeto 08 - Sistema de Gestão de Notas (Milestone 1 Completo) 🎓

## O Desafio 🎯
Uma escola precisa abandonar as planilhas de papel. Você deve criar o **SGN (Sistema de Gestão de Notas)** v1.0.

**Objetivo**: Consolidar **Vetores** e **Funções/Procedimentos** em um sistema com Menu Interativo.

## Requisitos Técnicos
1.  **Estrutura de Dados**:
    - Vetor `nomes[1..5]` (String)
    - Vetor `notas[1..5]` (Real)
2.  **Menu Principal** (Loop Infinito):
    1.  Cadastrar Aluno (Nome + Nota)
    2.  Listar Todos (Mostrar Tabela)
    3.  Mostrar Média da Turma (Função)
    4.  Sair
3.  **Modularização**:
    - Criar procedimento `MostrarMenu()`
    - Criar função `CalcularMediaTurma()` retorna Real.

## Cenário
O usuário inicia o programa. O sistema pergunta o que fazer.
Se escolher 1, pede o índice (1 a 5) e os dados.
Se escolher 2, percorre os vetores imprimindo "Aluno X: Nota Y".
Se escolher 3, soma tudo e divide por 5.

## Exemplo de Saída
```text
=== SGN v1.0 ===
1. Cadastrar
2. Listar
3. Média
4. Sair
Opção: 2

--- LISTA ---
1. Ana: 8.5
2. Bruno: 7.0
...
```

## Ferramenta
- VisualG.