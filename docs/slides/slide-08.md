# Aula 08 - Modularização 🧩

---

## Agenda 📅

1.  Dividir para Conquistar <!-- .element: class="fragment" -->
2.  Procedimentos (Sub-rotinas) <!-- .element: class="fragment" -->
3.  Funções (Retorno de valor) <!-- .element: class="fragment" -->
4.  Parâmetros e Escopo <!-- .element: class="fragment" -->
5.  Vantagens da Reutilização <!-- .element: class="fragment" -->

---

## 1. Dividir para Conquistar ⚔️

Problemas grandes devem ser fatiados:

- Facilita a leitura. <!-- .element: class="fragment" -->
- Facilita o teste. <!-- .element: class="fragment" -->
- Evita repetição de código (DRY - Don't Repeat Yourself). <!-- .element: class="fragment" -->

---

## 2. Procedimentos 🏃‍♂️

Executa uma tarefa e não devolve nada.

```visualg
Procedimento Topo()
Inicio
   escreval("----------------")
   escreval("  SISTEMA ABC   ")
   escreval("----------------")
FimProcedimento
```

---

## 3. Funções 🔄

Executa uma tarefa e **retorna** um valor.

```visualg
Funcao Soma(a, b : inteiro) : inteiro
Inicio
   Retorne a + b
FimFuncao
```

---

## 4. Escopo de Variáveis 🔍

- **Global**: Toda o programa enxerga. <!-- .element: class="fragment" -->
- **Local**: Só quem está dentro do módulo enxerga. <!-- .element: class="fragment" -->

---

## 5. Parâmetros 📬

Passagem de informação para dentro do módulo:

- **Por Valor**: Manda uma cópia. <!-- .element: class="fragment" -->
- **Por Referência**: Manda o endereço (altera o original). <!-- .element: class="fragment" -->

---

## Resumo ✅

- Procedimento: Executa ação. <!-- .element: class="fragment" -->
- Função: Calcula e devolve. <!-- .element: class="fragment" -->
- Escopo: Visibilidade da variável. <!-- .element: class="fragment" -->

---

## Final do Módulo 1! 🎉🏆

Você dominou a base de toda a tecnologia moderna.

---

## Próxima Aula (Módulo 2) 🚀

- **C / C++**: Entrando no mundo profissional e de baixo nível! <!-- .element: class="fragment" -->

👉 **Desafio**: Crie uma função que receba um número e retorne o seu dobro.