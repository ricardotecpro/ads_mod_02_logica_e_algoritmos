# Aula 05 - Estruturas Repetitivas 🔄

---

## Agenda 📅

1.  Por que repetir? <!-- .element: class="fragment" -->
2.  `Enquanto` (While) <!-- .element: class="fragment" -->
3.  `Repita` (Do While) <!-- .element: class="fragment" -->
4.  `Para` (For) <!-- .element: class="fragment" -->
5.  Contadores e Acumuladores <!-- .element: class="fragment" -->

---

## 1. Por que repetir? 🤔

Imagine imprimir de 1 a 1.000...

- Sem loops: 1.000 linhas de `escreva`. <!-- .element: class="fragment" -->
- Com loops: 3 linhas de código! <!-- .element: class="fragment" -->
- **Eficiência**: O computador não cansa de repetir. <!-- .element: class="fragment" -->

---

## 2. `Enquanto` (Com teste no início) 🏁

Só entra se for verdade. Pode nem rodar.

```visualg
c <- 1
Enquanto (c <= 10) faca
   escreva(c)
   c <- c + 1
FimEnquanto
```

---

## 3. `Repita` (Com teste no fim) 🏁

Roda pelo menos uma vez.

```visualg
c <- 1
Repita
   escreva(c)
   c <- c + 1
Ate (c > 10)
```

---

## 4. `Para` (Com contagem definida) 🔢

Ideal quando sabemos o fim.

```visualg
Para c de 1 ate 10 faca
   escreva(c)
FimPara
```

---

## 5. Contadores e Acumuladores 💰

- **Contador**: `c <- c + 1` (Soma de 1 em 1). <!-- .element: class="fragment" -->
- **Acumulador**: `soma <- soma + valor` (Soma valores variados). <!-- .element: class="fragment" -->

---

## Resumo ✅

- `Enquanto` testa antes. <!-- .element: class="fragment" -->
- `Repita` testa depois. <!-- .element: class="fragment" -->
- `Para` é automático. <!-- .element: class="fragment" -->

---

## Próxima Aula 🚀

- **Vetores**: Como guardar 100 nomes numa única variável? <!-- .element: class="fragment" -->

👉 **Desafio**: Faça a tabuada do 5 usando o loop `Para`.