# Aula 06 - Vetores (Arrays) 🧱

---

## Agenda 📅

1.  O que são Variáveis Compostas? <!-- .element: class="fragment" -->
2.  Declaração e Espaço em Memória <!-- .element: class="fragment" -->
3.  Acesso por Índice <!-- .element: class="fragment" -->
4.  Loops + Vetores (A união perfeita) <!-- .element: class="fragment" -->
5.  Prática: Lista de Nomes <!-- .element: class="fragment" -->

---

## 1. Variáveis Compostas Unidimensionais 📦

Até agora, 1 variável = 1 valor.

- **Problema**: E se eu quiser guardar 50 notas? <!-- .element: class="fragment" -->
- **Solução**: Vetores! <!-- .element: class="fragment" -->
- Um vetor é uma lista de elementos do **mesmo tipo**. <!-- .element: class="fragment" -->

---

## 2. Declaração 📝

No VisualG:

```visualg
Var
   v: vetor [1..5] de real
```

- Criou 5 "caixinhas" na memória. <!-- .element: class="fragment" -->
- Todas guardam números reais. <!-- .element: class="fragment" -->

---

## 3. Acesso por Índice 🔢

Como saber quem é quem?

- Cada posição tem um número (Índice). <!-- .element: class="fragment" -->
- No VisualG, começa em 1. <!-- .element: class="fragment" -->

```visualg
v[1] <- 10.5
v[2] <- 8.0
```

---

## 4. Loops + Vetores 🔄

Nunca use vetores sem loops!

```visualg
Para i de 1 ate 5 faca
   escreva("Digite o valor ", i, ": ")
   leia(v[i])
FimPara
```

---

## 5. Prática: Busca no Vetor 🔍

```visualg
Para i de 1 ate 5 faca
   Se (v[i] = "Carlos") Entao
      escreva("Encontrado na posicao ", i)
   FimSe
FimPara
```

---

## Resumo ✅

- Vantagem: Organização de muitos dados. <!-- .element: class="fragment" -->
- Índice: Localização do dado. <!-- .element: class="fragment" -->
- Loops: Automatizam a leitura e escrita. <!-- .element: class="fragment" -->

---

## Próxima Aula 🚀

- **Matrizes**: Tabelas com linhas e colunas! <!-- .element: class="fragment" -->

👉 **Desafio**: Crie um vetor que guarde 10 números e mostre apenas os Pares.