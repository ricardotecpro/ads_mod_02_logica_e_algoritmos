# Aula 04 - Estruturas Condicionais 🚦

---

## Agenda 📅

1.  O Poder da Escolha (`Se`) <!-- .element: class="fragment" -->
2.  Operadores Relacionais <!-- .element: class="fragment" -->
3.  Operadores Lógicos (`E`, `OU`, `NAO`) <!-- .element: class="fragment" -->
4.  Condicionais Compostas (`Senao`) <!-- .element: class="fragment" -->
5.  Escolha-Caso (Seleção Múltipla) <!-- .element: class="fragment" -->

---

## 1. O Comando `Se` (If) ❓

O programa decide se executa algo ou não.

```visualg
Se (idade >= 18) Entao
   escreva("Maior de Idade")
FimSe
```

---

## 2. Operadores Relacionais ⚖️

Usados para comparar valores:

- `>` : Maior que. <!-- .element: class="fragment" -->
- `<` : Menor que. <!-- .element: class="fragment" -->
- `>=` : Maior ou igual. <!-- .element: class="fragment" -->
- `<=` : Menor ou igual. <!-- .element: class="fragment" -->
- `=` : Igual. <!-- .element: class="fragment" -->
- `<>` : Diferente. <!-- .element: class="fragment" -->

---

## 3. Operadores Lógicos 🧠

Combinando condições:

- **E**: Tudo deve ser verdade. <!-- .element: class="fragment" -->
- **OU**: Apenas um precisa ser verdade. <!-- .element: class="fragment" -->
- **NÃO**: Inverte o valor. <!-- .element: class="fragment" -->

---

## 4. Condicional Composta 🌓

```visualg
Se (media >= 7) Entao
   escreva("Aprovado!")
Senao
   escreva("Reprovado!")
FimSe
```

---

## 5. Escolha-Caso 🗄️

Ideal para menus:

```visualg
Escolha (opcao)
Caso 1
   escreva("Soma")
Caso 2
   escreva("Subtracao")
OutroCaso
   escreva("Invalido")
FimEscolha
```

---

## Resumo ✅

- `Se` permite decisão. <!-- .element: class="fragment" -->
- `Senao` oferece alternativa. <!-- .element: class="fragment" -->
- Operadores relacionais comparam. <!-- .element: class="fragment" -->

---

## Próxima Aula 🚀

- **Estruturas de Repetição**: Chega de digitar o mesmo código 100 vezes! <!-- .element: class="fragment" -->

👉 **Desafio**: Crie um código que verifique se um número é Par ou Ímpar.