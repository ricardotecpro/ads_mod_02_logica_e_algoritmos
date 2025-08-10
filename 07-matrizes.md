# 🎛️ Matrizes (Arrays Bidimensionais) em Programação

Dando um passo além dos vetores (arrays de uma dimensão), as **matrizes** nos permitem trabalhar com dados estruturados em duas dimensões, como tabelas, planilhas ou tabuleiros.

## 🤔 O que são Matrizes?

[cite\_start]Uma matriz é uma coleção de dados que pode ser entendida como um **array bidimensional**[cite: 27]. Ela possui um conjunto de características fundamentais:

- [cite\_start]**Indexada**: Os elementos são acessados por meio de um par de índices: um para a linha e outro para a coluna[cite: 18]. Em Java, a sintaxe é `matriz[linha][coluna]`.
- [cite\_start]**Bidimensional**: Organiza os dados em uma estrutura de duas dimensões, composta por linhas e colunas[cite: 21].
- [cite\_start]**Homogênea**: Todos os dados armazenados na matriz devem ser do mesmo tipo (`int`, `double`, `String`, etc.)[cite: 24].
- [cite\_start]**Tamanho Fixo**: Uma vez que a matriz é criada (alocada na memória), seu tamanho (número de linhas e colunas) não pode ser alterado[cite: 26].

Visualmente, podemos imaginar uma matriz como uma grade:

```
      Col 0  Col 1  Col 2
Linha 0 [  ]   [  ]   [  ]
Linha 1 [  ]   [  ]   [  ]
Linha 2 [  ]   [  ]   [  ]
Linha 3 [  ]   [  ]   [  ]
```

## 🛠️ Trabalhando com Matrizes em Java

Vamos ver como declarar, instanciar e manipular matrizes na linguagem Java.

### Declaração e Instanciação

Para criar uma matriz, você precisa declarar seu tipo e, em seguida, instanciá-la, definindo seu número de linhas e colunas.

```java
// Sintaxe: tipo[][] nomeDaMatriz = new tipo[numeroDeLinhas][numeroDeColunas];

// Exemplo: Criando uma matriz de inteiros com 3 linhas e 4 colunas.
int[][] matriz = new int[3][4];
```

Isso aloca um espaço na memória para 12 números inteiros (3 linhas x 4 colunas).

### Acessando Elementos

Para atribuir ou ler um valor, você utiliza os índices da linha e da coluna. Lembre-se que em Java, **os índices sempre começam em zero**.

```java
// Atribuindo o valor 10 à segunda linha (índice 1), terceira coluna (índice 2)
matriz[1][2] = 10; [cite_start]// Equivalente ao A[1, 2] <- 10 do pseudocódigo [cite: 41]

// Lendo e imprimindo o valor
System.out.println(matriz[1][2]); // Saída: 10
```

## ✍️ Exemplo Prático: Lendo e Imprimindo uma Matriz

Vamos criar um programa que pergunta ao usuário as dimensões de uma matriz, lê cada um de seus elementos e, ao final, a imprime na tela de forma organizada.

**Problema:** Fazer um programa para ler dois números inteiros `M` e `N` e depois ler uma matriz de `M` linhas por `N` colunas contendo números inteiros. [cite\_start]Em seguida, mostrar a matriz lida[cite: 66, 67].

**Solução em Java:**

```java
package curso;

import java.util.Scanner;

public class LerMatriz {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Quantas linhas vai ter a matriz? ");
        int M = sc.nextInt();
        System.out.print("Quantas colunas vai ter a matriz? ");
        int N = sc.nextInt();

        // Instanciando a matriz com as dimensões informadas
        int[][] mat = new int[M][N];

        // Usando laços aninhados para ler os dados
        System.out.println("Digite os elementos da matriz:");
        for (int i = 0; i < M; i++) { // Laço para percorrer as linhas
            for (int j = 0; j < N; j++) { // Laço para percorrer as colunas
                System.out.printf("Elemento [%d,%d]: ", i, j);
                mat[i][j] = sc.nextInt();
            }
        }

        // Usando laços aninhados para imprimir a matriz
        System.out.println("\nMATRIZ DIGITADA:");
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(mat[i][j] + " "); // Imprime o elemento e um espaço
            }
            System.out.println(); // Pula para a próxima linha ao final de cada linha da matriz
        }

        sc.close();
    }
}
```

**Exemplo de Execução:**

```
Quantas linhas vai ter a matriz? 2
Quantas colunas vai ter a matriz? 3
Digite os elementos da matriz:
Elemento [0,0]: 5
Elemento [0,1]: 8
Elemento [0,2]: 10
Elemento [1,0]: -2
Elemento [1,1]: 9
Elemento [1,2]: 7

MATRIZ DIGITADA:
5 8 10 
-2 9 7 
```

## 🧠 Exercícios de Lógica com Matrizes

Vamos transformar alguns dos "testes de mesa" do material de estudo em programas Java funcionais para ver a lógica em ação.

### Exercício 1: Populando com uma Regra

**Problema:** Crie um programa que preenche uma matriz 3x3 onde o valor de cada elemento é a soma de seus índices (`linha + coluna`).

**Solução em Java:**

```java
package curso;

public class PopularMatrizRegra {

    public static void main(String[] args) {
        int N = 3;
        int[][] matriz = new int[N][N];

        // Populando a matriz com a regra mat[i][j] = i + j
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                matriz[i][j] = i + j; // Regra de população
            }
        }

        // Imprimindo a matriz resultante
        System.out.println("Matriz gerada:");
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }
}
```

**Saída Esperada:**

```
Matriz gerada:
0 1 2 
1 2 3 
2 3 4 
```

### Exercício 2: Soma dos Elementos de Cada Linha

**Problema:** Faça um programa que crie uma matriz 3x4, popule-a com valores, e em seguida, crie um **vetor** onde cada posição armazena a soma dos elementos da linha correspondente da matriz.

**Solução em Java:**

```java
package curso;

public class SomaLinhasMatriz {

    public static void main(String[] args) {
        int M = 3; // Linhas
        int N = 4; // Colunas

        int[][] matriz = {
            {5, 10, 2, 8},
            {4, 3, 9, 1},
            {7, 6, 5, 2}
        };

        // Vetor para armazenar a soma de cada linha
        int[] vetorSomas = new int[M];

        // Calculando a soma de cada linha
        for (int i = 0; i < M; i++) {
            int soma = 0;
            for (int j = 0; j < N; j++) {
                soma += matriz[i][j];
            }
            vetorSomas[i] = soma;
        }

        // Imprimindo o vetor com as somas
        System.out.println("Soma de cada linha:");
        for (int i = 0; i < M; i++) {
            System.out.printf("Linha %d: %d\n", i, vetorSomas[i]);
        }
    }
}
```

**Saída Esperada:**

```
Soma de cada linha:
Linha 0: 25
Linha 1: 17
Linha 2: 20
```

### 🛠️ Como Executar no VS Code e IntelliJ IDEA

Você pode compilar e executar todos os exemplos de código acima em qualquer uma das IDEs modernas.

#### No Visual Studio Code

1.  **Instale o Pacote de Extensões para Java**: Na aba de Extensões (`Ctrl+Shift+X`), procure por `Extension Pack for Java` da Microsoft e instale-o.
2.  **Crie o Arquivo**: Crie um novo arquivo com a extensão `.java` (ex: `LerMatriz.java`).
3.  **Cole o Código**: Copie e cole um dos exemplos no arquivo.
4.  **Execute**: Um botão **"Run"** aparecerá acima do método `main`. Clique nele para compilar e executar o código. A saída aparecerá no terminal integrado.

#### Na IntelliJ IDEA

1.  **Crie um Novo Projeto**: Vá em `File > New > Project`. Escolha `Java` e a versão do JDK.
2.  **Crie uma Nova Classe**: Na janela de projeto, clique com o botão direito na pasta `src`, vá em `New > Java Class` e dê um nome à classe (ex: `SomaLinhasMatriz`).
3.  **Cole o Código**: Copie e cole o código correspondente na classe criada.
4.  **Execute**: Clique com o botão direito do mouse em qualquer lugar dentro do editor de código e selecione **Run 'NomeDaClasse.main()'**. A saída aparecerá na aba "Run" na parte inferior da IDE.