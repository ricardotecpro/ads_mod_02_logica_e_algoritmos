# Estrutura Sequencial: O Começo de Tudo ➡️

Bem-vindo à sua primeira "aula de verdade" de lógica com código! Até agora, preparamos o terreno. Hoje, vamos aprender como um programa "pensa" da forma mais básica: um passo depois do outro.

## 1. O que é Estrutura Sequencial?

Imagine uma receita de bolo:
1.  Quebre os ovos.
2.  Bata a massa.
3.  Coloque no forno.

A ordem importa. Você não pode assar o bolo antes de quebrar os ovos. Na programação, a **Estrutura Sequencial** é isso: comandos executados **de cima para baixo**, uma linha de cada vez, sem pular nada.

---

## 2. Variáveis: As Caixas da Memória 📦

Para processar dados, o computador precisa guardá-los na memória RAM. Chamamos esses espaços de **Variáveis**.
Imagine uma variável como uma caixa etiquetada onde você guarda **UM** valor.

### Tipos de Dados Primitivos
Em Java (e na maioria das linguagens), as caixas têm tamanhos e formatos diferentes:

| Tipo | O que guarda? | Exemplo | Tamanho |
| :--- | :--- | :--- | :--- |
| **int** | Números inteiros | `10`, `-5`, `0` | Pequeno |
| **double** | Números com vírgula (Reais) | `10.5`, `3.1415` | Grande |
| **char** | Um único caractere | `'A'`, `'@'`, `'9'` | Minúsculo |
| **boolean** | Verdadeiro ou Falso | `true`, `false` | Mínimo |
| **String** | Texto (Palavras/Frases) | `"Olá Mundo"`, `"Mariana"` | Variável |

> **Nota**: `String` em Java é uma Classe especial, por isso começa com maiúscula.

### Declarando Variáveis

Sintaxe básica: `TIPO NOME_DA_VARIAVEL = VALOR;`

```java
int idade = 25;
double altura = 1.75;
char genero = 'F';
String nome = "Maria";
boolean estuda = true;
```

---

## 3. Entrada e Saída (Input/Output) 📤📥

Como o programa conversa com o usuário?

### Saída de Dados (Output)
É o que o programa mostra na tela.

```java
System.out.println("Olá, mundo!"); // Pula linha no final
System.out.print("Sem pular linha");
System.out.printf("Formatado: %.2f", 10.50); // %.2f = 2 casas decimais
```

### Entrada de Dados (Input)
É o que o usuário digita. Em Java, usamos um "scanner" para ler o teclado.

```java
import java.util.Scanner; // Importa a ferramenta Scanner

public class ExemploEntrada {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // Cria o leitor

        System.out.print("Digite seu nome: ");
        String nome = sc.next(); // Lê uma palavra

        System.out.print("Digite sua idade: ");
        int idade = sc.nextInt(); // Lê um inteiro

        System.out.println("Olá, " + nome + "! Você tem " + idade + " anos.");

        sc.close(); // Encerra o leitor
    }
}
```

---

## 4. Processamento de Dados (Cálculos) ➗

O processamento acontece através de **atribuições** e **expressões matemáticas**.

**Regra de Ouro**: O processamento (cálculo) deve acontecer **DA DIREITA PARA A ESQUERDA**.
*   `x = 10 + 5` -> Primeiro resolve `10 + 5`, depois guarda o `15` na caixa `x`.

### Operadores Aritméticos
*   `+` (Soma)
*   `-` (Subtração)
*   `*` (Multiplicação)
*   `/` (Divisão)
*   `%` (Módulo/Resto da Divisão) -> Útil para saber se um número é par ou ímpar (`x % 2 == 0`).

### Exemplo Completo: Soma de Dois Números

```java
import java.util.Scanner;

public class Soma {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x, y, soma; // Declarando múltiplas variáveis

        System.out.print("Digite o primeiro número: ");
        x = sc.nextInt();

        System.out.print("Digite o segundo número: ");
        y = sc.nextInt();

        soma = x + y; // Processamento

        System.out.println("SOMA = " + soma); // Saída

        sc.close();
    }
}
```

---

## 🧠 Exercícios de Fixação

1.  **Terreno**: Ler a largura e comprimento de um terreno, calcular a área (`largura * comprimento`) e o preço (`area * valor_metro`).
2.  **Média**: Ler 3 notas e calcular a média aritmética.

---
**Próxima Aula**: E se precisarmos tomar uma decisão? Aprenderemos a **Estrutura Condicional**.
