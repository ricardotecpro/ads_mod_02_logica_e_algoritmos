# Aula 03 - Estrutura Sequencial ➡️

---

## Agenda 📅

1.  Variáveis (Revisão) { .fragment }
2.  Tipos de Dados { .fragment }
3.  Entrada e Saída { .fragment }
4.  Operadores Aritméticos { .fragment }
5.  Atribuição { .fragment }

---

## 1. Variáveis: Caixas da Memória 📦

- Computador tem memória (RAM). { .fragment }
- **Variável**: Um pedaço nomeado dessa memória. { .fragment }
- Guardam **um valor** por vez. { .fragment }

---

### Visualização 🧪

```mermaid
graph TD;
    Memoria[RAM] --> Var1[Gaveta 'IDADE'];
    Var1 --> Val1[Valor: 25];
    Memoria --> Var2[Gaveta 'NOME'];
    Var2 --> Val2["Valor: 'Maria'"];
```

---

## 2. Tipos de Dados 📐

Nem tudo cabe na mesma caixa.

1.  **Inteiro**: Números sem vírgula (10, -5). { .fragment }
2.  **Real**: Números com vírgula (10.5, 3.14). { .fragment }
3.  **Caractere**: Texto ("Olá", "A"). { .fragment }
4.  **Lógico**: Verdadeiro ou Falso. { .fragment }

---

### Erro Comum ❌

Tentar colocar texto numa caixa de número.

```visualg
Var
   idade : inteiro
Inicio
   idade <- "Vinte" // ERRO!
```

---

## 3. Entrada e Saída ⚙️

Como o programa fala com o usuário?

- **Entrada**: Dados que entram (Teclado). { .fragment }
- **Saída**: Dados que saem (Tela). { .fragment }

---

### Comando: ESCREVA (Saída) 📤

- Mostra texto na tela. { .fragment }
- `escreva` (na mesma linha). { .fragment }
- `escreval` (pula linha). { .fragment }

```visualg
escreval("Olá Mundo")
escreva("Tudo bem?")
```

---

### Comando: LEIA (Entrada) 📥

- Pára o programa e espera o usuário digitar. { .fragment }
- Guarda o que foi digitado numa variável. { .fragment }

```visualg
escreva("Qual seu nome?")
leia(nome)
```

---

## 4. Atribuição (`<-`) ⬅️

- Colocar um valor dentro da variável. { .fragment }
- Lê-se: "Recebe". { .fragment }
- A seta sempre aponta para a esquerda (para a variável). { .fragment }

```visualg
media <- (n1 + n2) / 2
nome <- "João"
```

---

## 5. Operadores Aritméticos 🧮

O computador é uma calculadora gigante.

| Operador | Nome | Exemplo |
| :---: | :--- | :--- |
| `+` | Soma | `5 + 3` |
| `-` | Subtração | `10 - 2` |
| `*` | Multiplicação | `4 * 3` |
| `/` | Divisão | `20 / 4` |

---

### Operadores Especiais ✨

- **Módulo (`%`)**: Resto da divisão. { .fragment }
    - `5 % 2 = 1` (Sobrou 1). { .fragment }
    - Útil para saber se é Par ou Ímpar. { .fragment }
- **Potência (`^`)**: Elevar ao quadrado/cubo. { .fragment }
    - `2 ^ 3 = 8`. { .fragment }

---

## Ordem de Precedência 🥇

Matemática básica!

1.  Parênteses `( )` { .fragment }
2.  Potência `^` { .fragment }
3.  Multiplicação e Divisão `* /` { .fragment }
4.  Soma e Subtração `+ -` { .fragment }

> `2 + 3 * 4` = 14 (Não 20!)

---

## Exemplo Completo: Dobro do Número 🔢

Vamos criar um programa que lê um número e mostra o dobro.

---

### Passo 1: Definir Variáveis

```visualg
Algoritmo "Dobro"
Var
   numero : inteiro
   resultado : inteiro
```

---

### Passo 2: Entrada

```visualg
Inicio
   escreva("Digite um número: ")
   leia(numero)
```

---

### Passo 3: Processamento

```visualg
   resultado <- numero * 2
```

---

### Passo 4: Saída

```visualg
   escreval("O dobro é: ", resultado)
Fimalgoritmo
```

---

## Exercício Rápido ⚡

Faça no VisualG agora:
1.  Leia dois números. { .fragment }
2.  Some os dois. { .fragment }
3.  Mostre o resultado. { .fragment }

---

## Resumo ✅

- **Variáveis**: Nome, Tipo e Valor. { .fragment }
- **Tipos**: Inteiro, Real, Caractere, Lógico. { .fragment }
- **Entrada**: `leia()`. { .fragment }
- **Saída**: `escreva()`. { .fragment }
- **Atribuição**: `<-`. { .fragment }

---

## Próxima Aula 🚀

- E se precisarmos tomar **decisões**? { .fragment }
- O comando `SE`. { .fragment }
- Estruturas Condicionais. { .fragment }

👉 **Tarefa**: Terminar os exercícios da lista 03!