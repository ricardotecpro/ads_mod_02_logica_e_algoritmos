# Projeto 11 - Banco Imobiliário Simplificado ☕

!!! tip "Objetivo"
    **Objetivo**: Aplicar os pilares da Orientação a Objetos (Classes, Atributos, Métodos e Encapsulamento) em um cenário de simulação de jogo.

---

## O Desafio 🎯
Desenvolva uma versão simplificada (via terminal) de um jogo de compra e venda de propriedades. O foco aqui não é o visual, mas a interação entre objetos.

## Modelagem de Classes
1.  **Classe `Jogador`**:
    *   Atributos: `nome`, `saldo`, `posicaoAtual`.
    *   Métodos: `pagar(valor)`, `receber(valor)`, `mover(casas)`.
2.  **Classe `Propriedade`**:
    *   Atributos: `nome`, `precoCompra`, `valorAluguel`, `dono` (do tipo Jogador).

## Regras do Jogo
*   Crie 2 jogadores com saldo inicial de R$ 1000.
*   Simule rodadas usando um gerador de números aleatórios (Dados de 1 a 6).
*   **Se a casa não tem dono**: O jogador pode comprar (se tiver saldo).
*   **Se a casa tem dono**: O jogador deve pagar o aluguel ao dono da propriedade.
*   O jogo termina após 10 rodadas ou se alguém falir.

## Exemplo de Log no Terminal
```text
Jogador Ana caiu na casa 'Av. Paulista'.
Saldo insuficiente para compra.
Jogador Bruno caiu na casa 'Copacabana'.
Pagou R$ 50 de aluguel para Ana.
```

## Dica de Java 💡
Use `ArrayList<Propriedade>` para gerenciar o tabuleiro de forma dinâmica.