# Aula 07 - Matrizes (Tabelas) 📊

---

## Agenda 📅

1.  Variáveis Compostas Bidimensionais <!-- .element: class="fragment" -->
2.  Linhas e Colunas <!-- .element: class="fragment" -->
3.  Declaração de Matrizes <!-- .element: class="fragment" -->
4.  Percorrendo com Loops Aninhados <!-- .element: class="fragment" -->
5.  Prática: Jogo da Velha (Lógica) <!-- .element: class="fragment" -->

---

## 1. O que é uma Matriz? ⬛

É um vetor de vetores.

- Vetor = Linha única. <!-- .element: class="fragment" -->
- Matriz = Tabela (Linhas x Colunas). <!-- .element: class="fragment" -->
- Exemplo: Planilhas de Excel. <!-- .element: class="fragment" -->

---

## 2. Coordenadas 📍

Para acessar um valor, precisamos de dois números:

- **L**: Linha. <!-- .element: class="fragment" -->
- **C**: Coluna. <!-- .element: class="fragment" -->

> Acesso: `m[L, C]`

---

## 3. Declaração 📝

```visualg
Var
   m: vetor [1..3, 1..3] de inteiro
```
- Criou uma grade 3x3 (9 posições). <!-- .element: class="fragment" -->

---

## 4. Loops Aninhados 🔄🔄

Para ler uma matriz, usamos um loop dentro do outro:

```visualg
Para l de 1 ate 3 faca
   Para c de 1 ate 3 faca
      leia(m[l,c])
   FimPara
FimPara
```

---

## 5. Prática: Soma Diagonal 📉

```visualg
soma <- 0
Para i de 1 ate 3 faca
   soma <- soma + m[i,i]
FimPara
```

---

## Resumo ✅

- Matriz = Linhas + Colunas. <!-- .element: class="fragment" -->
- Precisa de dois índices. <!-- .element: class="fragment" -->
- Loops duplos facilitam o manuseio. <!-- .element: class="fragment" -->

---

## Próxima Aula 🚀

- **Modularização**: Dividir para conquistar! Procedimentos e Funções. <!-- .element: class="fragment" -->

👉 **Desafio**: Pense em como representar um tabuleiro de Xadrez em código.