# Projeto 07 - Jogo da Velha (Tic-Tac-Toe) ⭕❌

!!! tip "Objetivo"
    **Objetivo**: Aplicar o conceito de Matrizes (vetores bidimensionais) para gerenciar um tabuleiro de jogo e verificar condições de vitória em grade.

---

## O Desafio 🎯
Você deve programar o clássico Jogo da Velha. Este é o desafio definitivo sobre coordenadas (Linhas e Colunas).

## Requisitos Técnicos
1.  **Tabuleiro**: Use uma matriz 3x3 de caracteres (char). Comece preenchendo-a com espaços vazios ou traços `-`.
2.  **Alternância**: O programa deve alternar entre o Jogador 1 (X) e o Jogador 2 (O).
3.  **Entrada**: O jogador deve digitar a Linha (1, 2 ou 3) e a Coluna (1, 2 ou 3) onde deseja jogar.
4.  **Validação**: Não permita jogar em uma casa que já esteja ocupada.
5.  **Condição de Fim**:
    *   **Vitória**: Verifique se há 3 símbolos iguais em linha, coluna ou diagonal.
    *   **Empate (Velha)**: Verifique se o tabuleiro encheu sem nenhum ganhador.

## Visual do Tabuleiro (Exemplo)
Ao rodar, o sistema deve desenhar algo como:
```text
  1 2 3
1 X| |O
  -----
2  |X| 
  -----
3  | |O
```

## Dica Crucial 💡
Crie uma função ou procedimento chamado `DesenharTabuleiro()` para que você possa chamá-lo após cada jogada sem repetir código!