# Aula 03 - Estrutura Sequencial ➡️

!!! tip "Objetivo"
    **Objetivo**: Entender como o computador guarda informações (Variáveis) e executa comandos um após o outro.

---

## 1. Variáveis: As Caixas da Memória 📦

Imagine que a memória RAM do computador é um grande **armário cheio de gavetas**. Cada gaveta tem um endereço e guarda **uma coisa** por vez.

### Visualizando a Memória (Mermaid)

```mermaid
graph TD;
    Memoria[Memória RAM] --> Var1[Gaveta 'IDADE'];
    Var1 --> Val1[Valor: 25];
    Memoria --> Var2[Gaveta 'NOME'];
    Var2 --> Val2["Valor: 'Maria'"];
    
    style Var1 fill:#f9f,stroke:#333;
    style Var2 fill:#bbf,stroke:#333;
```

---

## 2. Tipos de Dados (O Formato da Caixa) 📐

Nem tudo cabe na mesma gaveta. Precisamos definir o **TIPO** da variável.

| Tipo (Pseudocódigo) | O que guarda? | Exemplo | Tamanho (Bytes) |
| :--- | :--- | :--- | :---: |
| **Inteiro** | Números sem vírgula | `10`, `-5`, `0` | 4 |
| **Real** | Números com vírgula | `10.5`, `3.14` | 8 |
| **Caractere** | Texto (Letras/Palavras) | `"Olá"`, `'A'` | Var |
| **Lógico** | Verdadeiro ou Falso | `VERDADEIRO` | 1 |

!!! warning "Erro Comum"
    **Erro Comum**: Tentar guardar texto numa variável numérica gera erro! `inteiro x = "texto"` ❌

---

## 3. Entrada, Processamento e Saída ⚙️

Todo algoritmo segue esse fluxo:

1.  **Entrada (Input)**: Dados que chegam (Teclado, Arquivo).
2.  **Processamento**: Cálculos (`soma = a + b`).
3.  **Saída (Output)**: Resultado (Tela).

### Exemplo: Calculadora de Dobro (VisualG)

```portugol
Algoritmo "Dobro"
Var
   num, resultado : inteiro
Inicio
   // Entrada
   escreva("Digite um número: ")
   leia(num)
   
   // Processamento
   resultado <- num * 2
   
   // Saída
   escreva("O dobro é: ", resultado)
Fimalgoritmo
```

### Simulando a Execução (Termynal)

<div data-termynal class="termy">
    <span data-ty="input">./calcula_dobro</span>
    <span data-ty>Digite um número: 5</span>
    <span data-ty="progress">O dobro é: 10</span>
</div>

---

## 4. Operadores Aritméticos 🧮

O computador é uma calculadora gigante.

| Operador | Nome | Exemplo | Resultado |
| :---: | :--- | :--- | :--- |
| `+` | Soma | `5 + 3` | `8` |
| `-` | Subtração | `10 - 2` | `8` |
| `*` | Multiplicação | `4 * 2` | `8` |
| `/` | Divisão | `16 / 2` | `8` |
| `%` | Módulo (Resto) | `5 % 2` | `1` (Sobrou 1) |
| `^` | Potência | `2 ^ 3` | `8` |

!!! tip "Dica: Resto da Divisão"
    O operador `%` é muito útil para saber se um número é **Par** ou **Ímpar**.
    *   `x % 2 = 0` -> Par
    *   `x % 2 = 1` -> Ímpar

---

## 5. Matemática Computacional (MathJax) 📐

Os computadores são EXCELENTES em resolver fórmulas complexas. Um exemplo famoso na Engenharia de Software é o **Modelo COCOMO**, usado para estimar o esforço de um projeto:

!!! info "Fórmula de Es esforço"
    A fórmula básica para estimar o esforço em meses/pessoa é:
    $$ E = a \cdot (KLOC)^b $$
    Onde:
    
    *   $E$: Esforço (meses/pessoa)
    *   $KLOC$: Milhares de linhas de código
    *   $a, b$: Constantes do projeto

---

## 6. Mini-Projeto: O Conversor Universal 🚀

Agora que você sabe usar variáveis e operadores, vamos criar uma ferramenta útil.

!!! info "Desafio do Projeto"
    Crie um algoritmo (Pseudocódigo) que receba um valor em **Reais (R$)** e mostre quanto esse valor vale em **Dólares (US$)** e **Euros (€)**. 
    Considere cotações fixas para o teste (ex: US$ 1.00 = R$ 5.00).

---

## 7. Exercícios de Fixação 📝

1.  **Fácil**: Crie um algoritmo que leia o **Nome** e **Idade** de, pessoa e mostre: "Olá [Nome], você tem [Idade] anos".
2.  **Médio**: Leia dois números (A e B) e troque seus valores (A vira B, B vira A).
    ??? tip "Dica da Troca"
        Imagine dois copos (um com suco, outro com água). Para trocar o conteúdo, você precisa de um **terceiro copo vazio** (variável auxiliar)!
3.  **Desafio**: Um motorista deseja encher o tanque. Leia o preço da gasolina e o valor que ele tem em dinheiro. Calcule quantos litros ele consegue colocar.

---
**Próxima Aula**: E se precisarmos tomar decisões? [Estrutura Condicional](./aula-04.md).