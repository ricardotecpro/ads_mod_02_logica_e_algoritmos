# Projeto 05 - Jogo de Adivinhação 🎲

!!! tip "Objetivo"
    **Objetivo**: Implementar a lógica de repetição e controle de fluxo através de um jogo interativo que utiliza números aleatórios.

---

## O Desafio 🎯
Desenvolva um jogo onde o computador escolhe um número secreto e desafia o usuário a descobri-lo. O programa deve dar dicas se o chute foi muito alto ou muito baixo.

## Requisitos Técnicos
1.  **Geração Aleatória**: O computador deve sortear um número entre 1 e 100.
2.  **Loop Principal**: O jogo não deve fechar até que o usuário acerte o número.
3.  **Dicas Inteligentes**:
    *   Se o chute for maior que o número: Exibir "Tente um número MENOR!".
    *   Se o chute for menor que o número: Exibir "Tente um número MAIOR!".
4.  **Contador**: Ao final, o programa deve informar quantas tentativas foram necessárias.

## Fluxo do Algoritmo
- [ ] Inicia o contador em 0.
- [ ] Sorteia o número secreto.
- [ ] Inicia um loop (Enquanto chute != secreto).
- [ ] Lê o chute do usuário e incrementa o contador.
- [ ] Compara e dá a dica.
- [ ] Se acertou, sai do loop e mostra a mensagem de vitória.

## Diferencial (Desafio Extra) ⭐
Adicione um limite de 10 tentativas. Se o usuário não acertar até lá, ele perde o jogo!