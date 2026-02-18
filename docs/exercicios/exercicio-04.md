# 📝 Exercícios de Estruturas Repetitivas

## Parte 1: Estrutura `enquanto` 🔁

### Problema "crescente" 📈

Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Para cada dupla, exiba "CRESCENTE" se X for menor que Y, ou "DECRESCENTE" caso contrário. O programa deve finalizar quando forem digitados dois valores iguais.

**Exemplo:**

```
Digite dois números:
10
2
DECRESCENTE!

Digite outros dois números:
7
11
CRESCENTE!

Digite outros dois números:
5
5
```

#### Solução em Java

```java
package exercicios;

import java.util.Scanner;

public class Crescente {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int x, y;

        System.out.println("Digite dois números:");
        x = entrada.nextInt();
        y = entrada.nextInt();

        while (x != y) {
            if (x < y) {
                System.out.println("CRESCENTE!");
            } else {
                System.out.println("DECRESCENTE!");
            }
            System.out.println("\nDigite outros dois números:");
            x = entrada.nextInt();
            y = entrada.nextInt();
        }
        
        entrada.close();
    }
}
```

### Problema "media\_idades" 👵

Faça um programa para ler um número indeterminado de idades. O programa para quando uma idade negativa for digitada. Calcule e imprima a idade média do grupo. Se a primeira idade digitada for negativa, mostre a mensagem "IMPOSSIVEL CALCULAR".

**Exemplo 1:**

```
Digite as idades:
35
28
49
-10
MEDIA = 37.33
```

**Exemplo 2:**

```
Digite as idades:
-15
IMPOSSIVEL CALCULAR
```

#### Solução em Java

```java
package exercicios;

import java.util.Locale;
import java.util.Scanner;

public class MediaIdades {

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner entrada = new Scanner(System.in);
        
        int idade, totalPessoas = 0, somaIdades = 0;
        double media;

        System.out.println("Digite as idades:");
        idade = entrada.nextInt();

        if (idade < 0) {
            System.out.println("IMPOSSIVEL CALCULAR");
        } else {
            while (idade >= 0) {
                somaIdades += idade;
                totalPessoas++;
                idade = entrada.nextInt();
            }
            media = (double) somaIdades / totalPessoas;
            System.out.printf("MEDIA = %.2f\n", media);
        }

        entrada.close();
    }
}
```

### Problema "senha\_fixa" 🔐

Escreva um programa que repita a leitura de uma senha até que ela seja válida. A senha correta é **2002**. Para cada tentativa incorreta, exiba "Senha Invalida\! Tente novamente:". Quando a senha for correta, mostre "Acesso Permitido" e termine o programa.

**Exemplo:**

```
Digite a senha:
2315
Senha Invalida! Tente novamente:
2024
Senha Invalida! Tente novamente:
2002
Acesso Permitido
```

#### Solução em Java

```java
package exercicios;

import java.util.Scanner;

public class SenhaFixa {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int senha;

        System.out.print("Digite a senha: \n");
        senha = entrada.nextInt();

        while (senha != 2002) {
            System.out.print("Senha Invalida! Tente novamente:\n");
            senha = entrada.nextInt();
        }

        System.out.println("Acesso Permitido");

        entrada.close();
    }
}
```

### Problema "quadrante" 🧭

Escreva um programa para ler as coordenadas (X, Y) de uma quantidade indeterminada de pontos. Para cada ponto, informe o quadrante ao qual ele pertence (Q1, Q2, Q3 ou Q4). O programa encerra quando uma das coordenadas for nula.

**Exemplo:**

```
Digite os valores das coordenadas X e Y:
3
4
QUADRANTE Q1

Digite os valores das coordenadas X e Y:
-5
2
QUADRANTE Q2

Digite os valores das coordenadas X e Y:
0
5
```

#### Solução em Java

```java
package exercicios;

import java.util.Scanner;

public class Quadrante {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int x, y;

        System.out.println("Digite os valores das coordenadas X e Y:");
        x = entrada.nextInt();
        y = entrada.nextInt();

        while (x != 0 && y != 0) {
            if (x > 0 && y > 0) {
                System.out.println("QUADRANTE Q1");
            } else if (x < 0 && y > 0) {
                System.out.println("QUADRANTE Q2");
            } else if (x < 0 && y < 0) {
                System.out.println("QUADRANTE Q3");
            } else {
                System.out.println("QUADRANTE Q4");
            }
            
            System.out.println("\nDigite os valores das coordenadas X e Y:");
            x = entrada.nextInt();
            y = entrada.nextInt();
        }

        entrada.close();
    }
}
```

### Problema "validacao\_de\_nota" 🎓

Faça um programa que leia as duas notas de um aluno. O programa deve validar cada nota individualmente, aceitando apenas valores no intervalo [0,10]. Se uma nota inválida for digitada, o programa deve pedir para digitá-la novamente. Ao final, calcule e imprima a média semestral.

**Exemplo:**

```
Digite a primeira nota: -4.5
Valor invalido! Tente novamente: 12.0
Valor invalido! Tente novamente: 8.0
Digite a segunda nota: 9.5
MEDIA = 8.75
```

#### Solução em Java

```java
package exercicios;

import java.util.Locale;
import java.util.Scanner;

public class ValidacaoDeNota {

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner entrada = new Scanner(System.in);
        double nota1, nota2, media;

        System.out.print("Digite a primeira nota: ");
        nota1 = entrada.nextDouble();
        while (nota1 < 0 || nota1 > 10) {
            System.out.print("Valor invalido! Tente novamente: ");
            nota1 = entrada.nextDouble();
        }

        System.out.print("Digite a segunda nota: ");
        nota2 = entrada.nextDouble();
        while (nota2 < 0 || nota2 > 10) {
            System.out.print("Valor invalido! Tente novamente: ");
            nota2 = entrada.nextDouble();
        }
        
        media = (nota1 + nota2) / 2.0;
        System.out.printf("MEDIA = %.2f\n", media);

        entrada.close();
    }
}
```

### Problema "combustivel" ⛽

Um posto de combustíveis deseja saber a preferência de seus clientes. Escreva um programa para ler o tipo de combustível abastecido, codificado como: **1.Álcool**, **2.Gasolina**, **3.Diesel**, **4.Fim**. Caso o usuário informe um código inválido, um novo código deve ser solicitado. O programa será encerrado quando o código informado for `4`, mostrando a quantidade de clientes que abasteceu cada tipo de combustível.

**Exemplo:**

```
Informe um codigo (1, 2, 3) ou 4 para parar: 1
Informe um codigo (1, 2, 3) ou 4 para parar: 2
Informe um codigo (1, 2, 3) ou 4 para parar: 2
Informe um codigo (1, 2, 3) ou 4 para parar: 9
Informe um codigo (1, 2, 3) ou 4 para parar: 3
Informe um codigo (1, 2, 3) ou 4 para parar: 4
MUITO OBRIGADO
Alcool: 1
Gasolina: 2
Diesel: 1
```

#### Solução em Java

```java
package exercicios;

import java.util.Scanner;

public class Combustivel {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int codigo;
        int alcool = 0;
        int gasolina = 0;
        int diesel = 0;

        System.out.print("Informe um codigo (1, 2, 3) ou 4 para parar: ");
        codigo = entrada.nextInt();

        while (codigo != 4) {
            switch (codigo) {
                case 1:
                    alcool++;
                    break;
                case 2:
                    gasolina++;
                    break;
                case 3:
                    diesel++;
                    break;
            }
            System.out.print("Informe um codigo (1, 2, 3) ou 4 para parar: ");
            codigo = entrada.nextInt();
        }

        System.out.println("MUITO OBRIGADO");
        System.out.println("Alcool: " + alcool);
        System.out.println("Gasolina: " + gasolina);
        System.out.println("Diesel: " + diesel);

        entrada.close();
    }
}
```

## Parte 2: Estrutura `para` 🔄

### Problema "tabuada" ✖️

Ler um número inteiro N e mostrar na tela a tabuada de N de 1 a 10.

**Exemplo:**

```
Deseja a tabuada para qual valor? 7
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

#### Solução em Java

```java
package exercicios;

import java.util.Scanner;

public class Tabuada {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int n;

        System.out.print("Deseja a tabuada para qual valor? ");
        n = entrada.nextInt();

        for (int i = 1; i <= 10; i++) {
            System.out.printf("%d x %d = %d\n", n, i, n * i);
        }

        entrada.close();
    }
}
```

### Problema "soma\_impares" ➕

Leia 2 valores inteiros X e Y em qualquer ordem. A seguir, calcule e mostre a soma dos números ímpares entre eles (sem incluir X e Y).

**Exemplo 1:**

```
Digite dois numeros:
3
10
SOMA DOS IMPARES = 21
```

*Observação: Ímpares entre 3 e 10 são 5, 7, 9. Soma = 21*

**Exemplo 2:**

```
Digite dois numeros:
18
12
SOMA DOS IMPARES = 45
```

*Observação: Ímpares entre 12 e 18 são 13, 15, 17. Soma = 45*

#### Solução em Java

```java
package exercicios;

import java.util.Scanner;

public class SomaImpares {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int x, y, troca, soma;

        System.out.println("Digite dois numeros:");
        x = entrada.nextInt();
        y = entrada.nextInt();

        if (x > y) {
            troca = x;
            x = y;
            y = troca;
        }

        soma = 0;
        for (int i = x + 1; i < y; i++) {
            if (i % 2 != 0) {
                soma += i;
            }
        }

        System.out.println("SOMA DOS IMPARES = " + soma);
        entrada.close();
    }
}
```

### Problema "sequencia\_impares" 📉

Leia um valor inteiro X e mostre os números ímpares de 1 até X, um valor por linha.

**Exemplo:**

```
Digite o valor de X: 10
1
3
5
7
9
```

#### Solução em Java

```java
package exercicios;

import java.util.Scanner;

public class SequenciaImpares {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int x;

        System.out.print("Digite o valor de X: ");
        x = entrada.nextInt();

        for (int i = 1; i <= x; i++) {
            if (i % 2 != 0) {
                System.out.println(i);
            }
        }

        entrada.close();
    }
}
```

### Problema "dentro\_fora" 🎯

Leia um valor inteiro N, que indica a quantidade de valores inteiros X que serão lidos a seguir. Mostre quantos desses valores X estão dentro do intervalo [10, 20] e quantos estão fora.

**Exemplo:**

```
Quantos numeros voce vai digitar? 6
Digite um numero: 15
Digite um numero: 40
Digite um numero: 10
Digite um numero: 25
Digite um numero: 8
Digite um numero: 20
3 DENTRO
3 FORA
```

#### Solução em Java

```java
package exercicios;

import java.util.Scanner;

public class DentroFora {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int n, x, dentro = 0, fora = 0;

        System.out.print("Quantos numeros voce vai digitar? ");
        n = entrada.nextInt();

        for (int i = 0; i < n; i++) {
            System.out.print("Digite um numero: ");
            x = entrada.nextInt();
            if (x >= 10 && x <= 20) {
                dentro++;
            } else {
                fora++;
            }
        }

        System.out.println(dentro + " DENTRO");
        System.out.println(fora + " FORA");

        entrada.close();
    }
}
```

### Problema "par\_impar" ☯️

Leia um valor inteiro N, que representa a quantidade de números que serão lidos. Para cada valor, mostre se é PAR ou ÍMPAR e se é POSITIVO ou NEGATIVO. Se o valor for zero, imprima "NULO".

**Exemplo:**

```
Quantos numeros voce vai digitar? 5
Digite um numero: -8
PAR NEGATIVO
Digite um numero: 7
IMPAR POSITIVO
Digite um numero: 0
NULO
```

#### Solução em Java

```java
package exercicios;

import java.util.Scanner;

public class ParImpar {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int n, x;

        System.out.print("Quantos numeros voce vai digitar? ");
        n = entrada.nextInt();

        for (int i = 0; i < n; i++) {
            System.out.print("Digite um numero: ");
            x = entrada.nextInt();

            if (x == 0) {
                System.out.println("NULO");
            } else {
                if (x % 2 == 0) {
                    System.out.print("PAR ");
                } else {
                    System.out.print("IMPAR ");
                }

                if (x > 0) {
                    System.out.println("POSITIVO");
                } else {
                    System.out.println("NEGATIVO");
                }
            }
        }

        entrada.close();
    }
}
```

### Problema "media\_ponderada" ⚖️

Leia um valor N que representa o número de casos de teste. Cada caso consiste em 3 valores reais, para os quais você deve calcular e mostrar a média ponderada. O primeiro valor tem peso 2, o segundo tem peso 3 e o terceiro tem peso 5.

**Exemplo:**

```
Quantos casos voce vai digitar? 3
Digite tres numeros:
7.0 5.0 8.0
MEDIA = 6.9
Digite tres numeros:
6.0 4.5 9.0
MEDIA = 6.9
```

#### Solução em Java

```java
package exercicios;

import java.util.Locale;
import java.util.Scanner;

public class MediaPonderada {

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner entrada = new Scanner(System.in);
        int n;

        System.out.print("Quantos casos voce vai digitar? ");
        n = entrada.nextInt();

        for (int i = 0; i < n; i++) {
            System.out.println("Digite tres numeros:");
            double v1 = entrada.nextDouble();
            double v2 = entrada.nextDouble();
            double v3 = entrada.nextDouble();

            double media = (v1 * 2.0 + v2 * 3.0 + v3 * 5.0) / 10.0;
            System.out.printf("MEDIA = %.1f\n", media);
        }

        entrada.close();
    }
}
```

### Problema "divisao" ➗

Escreva um algoritmo que leia um número N e, em seguida, N pares de números. Para cada par, imprima o resultado da divisão do primeiro pelo segundo. Caso a divisão não seja possível (denominador zero), mostre "DIVISAO IMPOSSIVEL".

**Exemplo:**

```
Quantos casos voce vai digitar? 3
Entre com o numerador: 10
Entre com o denominador: -2
DIVISAO = -5.00
Entre com o numerador: -9
Entre com o denominador: 0
DIVISAO IMPOSSIVEL
```

#### Solução em Java

```java
package exercicios;

import java.util.Locale;
import java.util.Scanner;

public class Divisao {

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner entrada = new Scanner(System.in);
        int n;

        System.out.print("Quantos casos voce vai digitar? ");
        n = entrada.nextInt();

        for (int i = 0; i < n; i++) {
            System.out.print("Entre com o numerador: ");
            int numerador = entrada.nextInt();
            System.out.print("Entre com o denominador: ");
            int denominador = entrada.nextInt();

            if (denominador == 0) {
                System.out.println("DIVISAO IMPOSSIVEL");
            } else {
                double divisao = (double) numerador / denominador;
                System.out.printf("DIVISAO = %.2f\n", divisao);
            }
        }

        entrada.close();
    }
}
```

### Problema "fatorial" ❗

Faça um programa para ler um número natural N (valor máximo 15) e depois calcular e mostrar o fatorial de N.

**Exemplo:**

```
Digite o valor de N: 5
FATORIAL = 120
```

#### Solução em Java

```java
package exercicios;

import java.util.Scanner;

public class Fatorial {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int n, fatorial;

        System.out.print("Digite o valor de N: ");
        n = entrada.nextInt();

        fatorial = 1;
        for (int i = n; i > 0; i--) {
            fatorial = fatorial * i;
        }

        System.out.println("FATORIAL = " + fatorial);

        entrada.close();
    }
}
```

### Problema "experiencias" 🔬

Um laboratório utiliza três tipos de cobaias: sapos, ratos e coelhos. Faça um programa que leia um número N de casos de teste. Cada caso informa a quantidade de cobaias e o tipo ('C', 'R' ou 'S'). Ao final, apresente um relatório com:

  - O total de cobaias utilizadas.
  - O total de cada tipo de cobaia.
  - O percentual de cada tipo em relação ao total, com duas casas decimais.

**Exemplo:**

```
Quantos casos de teste serao digitados? 8
Quantidade de cobaias: 12
Tipo de cobaia: C
...
RELATORIO FINAL:
Total: 78 cobaias
Total de coelhos: 29
Total de ratos: 28
Total de sapos: 21
Percentual de coelhos: 37.18 %
Percentual de ratos: 35.90 %
Percentual de sapos: 26.92 %
```

#### Solução em Java

```java
package exercicios;

import java.util.Locale;
import java.util.Scanner;

public class Experiencias {

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner entrada = new Scanner(System.in);
        
        int n, quantidade;
        char tipo;
        int totalCoelhos = 0;
        int totalRatos = 0;
        int totalSapos = 0;
        
        System.out.print("Quantos casos de teste serao digitados? ");
        n = entrada.nextInt();

        for (int i = 0; i < n; i++) {
            System.out.print("Quantidade de cobaias: ");
            quantidade = entrada.nextInt();
            System.out.print("Tipo de cobaia: ");
            tipo = entrada.next().charAt(0);

            if (tipo == 'C') {
                totalCoelhos += quantidade;
            } else if (tipo == 'R') {
                totalRatos += quantidade;
            } else if (tipo == 'S') {
                totalSapos += quantidade;
            }
        }
        
        int totalCobaias = totalCoelhos + totalRatos + totalSapos;
        double pCoelhos = (double) totalCoelhos / totalCobaias * 100.0;
        double pRatos = (double) totalRatos / totalCobaias * 100.0;
        double pSapos = (double) totalSapos / totalCobaias * 100.0;

        System.out.println("\nRELATORIO FINAL:");
        System.out.println("Total: " + totalCobaias + " cobaias");
        System.out.println("Total de coelhos: " + totalCoelhos);
        System.out.println("Total de ratos: " + totalRatos);
        System.out.println("Total de sapos: " + totalSapos);
        System.out.printf("Percentual de coelhos: %.2f %%\n", pCoelhos);
        System.out.printf("Percentual de ratos: %.2f %%\n", pRatos);
        System.out.printf("Percentual de sapos: %.2f %%\n", pSapos);
        
        entrada.close();
    }
}
```

-----

### 🚀 [ricardotecpro.github.io](https://www.google.com/search?q=https://ricardotecpro.github.io/)

# 🔄 Exercícios Resolvidos com Estruturas Repetitivas em Java

Este documento apresenta uma coleção de problemas e suas respectivas soluções em Java, focando no uso das estruturas de repetição `while` e `for`. Cada exercício foi adaptado de desafios de programação para reforçar a lógica e a aplicação prática desses conceitos.

> **Atenção:** Nos exemplos de execução, os dados em **vermelho** representam os valores digitados pelo usuário no console.

## Parte 1: Estrutura `while`

A estrutura `while` é ideal para situações em que não sabemos de antemão quantas vezes um bloco de código precisa ser repetido. A repetição continua enquanto uma determinada condição for verdadeira.

### 1\. Problema "crescente"

**Descrição:** Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada dupla uma mensagem que indique se os valores foram digitados em ordem crescente ou decrescente. O programa termina quando os dois valores digitados forem iguais.

#### Solução em Java

```java
package exercicios;

import java.util.Scanner;

public class Crescente {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite dois números:");
        int x = sc.nextInt();
        int y = sc.nextInt();

        while (x != y) {
            if (x < y) {
                System.out.println("CRESCENTE!");
            } else {
                System.out.println("DECRESCENTE!");
            }
            System.out.println("Digite outros dois números:");
            x = sc.nextInt();
            y = sc.nextInt();
        }
        sc.close();
    }
}
```

#### Exemplo de Execução

```
Digite dois números:
5
4
DECRESCENTE!
Digite outros dois números:
3
8
CRESCENTE!
Digite outros dois números:
2
2
```

### 2\. Problema "media\_idades"

**Descrição:** Faça um programa para ler um número indeterminado de idades. O programa para quando uma idade negativa é digitada (este valor não entra no cálculo). Calcule e imprima a idade média do grupo. Se a primeira idade digitada for negativa, mostre a mensagem "IMPOSSIVEL CALCULAR".

#### Solução em Java

```java
package exercicios;

import java.util.Locale;
import java.util.Scanner;

public class MediaIdades {

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite as idades:");
        int idade = sc.nextInt();
        
        if (idade < 0) {
            System.out.println("IMPOSSIVEL CALCULAR");
        } else {
            int soma = 0;
            int count = 0;
            while (idade >= 0) {
                soma += idade;
                count++;
                idade = sc.nextInt();
            }
            double media = (double) soma / count;
            System.out.printf("MEDIA = %.2f\n", media);
        }
        sc.close();
    }
}
```

#### Exemplo de Execução

```
Digite as idades:
31
27
46
-5
MEDIA = 34.67
```

### 3\. Problema "senha\_fixa"

**Descrição:** Escreva um programa que repita a leitura de uma senha até que ela seja válida. A senha correta é **2002**. Para cada tentativa incorreta, informe "Senha Invalida\! Tente novamente:". Quando a senha estiver correta, mostre "Acesso Permitido" e encerre o programa.

#### Solução em Java

```java
package exercicios;

import java.util.Scanner;

public class SenhaFixa {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite a senha: ");
        int senha = sc.nextInt();

        while (senha != 2002) {
            System.out.print("Senha Invalida! Tente novamente: ");
            senha = sc.nextInt();
        }

        System.out.println("Acesso Permitido");
        sc.close();
    }
}
```

#### Exemplo de Execução

```
Digite a senha: 2312
Senha Invalida! Tente novamente: 2010
Senha Invalida! Tente novamente: 2002
Acesso Permitido
```

### 4\. Problema "quadrante"

**Descrição:** Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos. Para cada ponto, escreva o quadrante ao qual ele pertence (Q1, Q2, Q3 ou Q4). O algoritmo será encerrado quando uma das coordenadas for NULA.

#### Solução em Java

```java
package exercicios;

import java.util.Scanner;

public class Quadrante {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite os valores das coordenadas X e Y:");
        int x = sc.nextInt();
        int y = sc.nextInt();

        while (x != 0 && y != 0) {
            if (x > 0 && y > 0) {
                System.out.println("QUADRANTE Q1");
            } else if (x < 0 && y > 0) {
                System.out.println("QUADRANTE Q2");
            } else if (x < 0 && y < 0) {
                System.out.println("QUADRANTE Q3");
            } else {
                System.out.println("QUADRANTE Q4");
            }
            System.out.println("Digite os valores das coordenadas X e Y:");
            x = sc.nextInt();
            y = sc.nextInt();
        }
        sc.close();
    }
}
```

#### Exemplo de Execução

```
Digite os valores das coordenadas X e Y:
2
2
QUADRANTE Q1
Digite os valores das coordenadas X e Y:
3
-2
QUADRANTE Q4
Digite os valores das coordenadas X e Y:
-8
-1
QUADRANTE Q3
Digite os valores das coordenadas X e Y:
-7
1
QUADRANTE Q2
Digite os valores das coordenadas X e Y:
0
2
```

### 5\. Problema "combustivel"

**Descrição:** Um posto de combustíveis deseja saber a preferência de seus clientes. Leia o tipo de combustível abastecido (1.Álcool, 2.Gasolina, 3.Diesel, 4.Fim). Caso o usuário informe um código inválido, peça um novo código até que seja válido. O programa encerra quando o código for 4, mostrando a mensagem "MUITO OBRIGADO" e as quantidades de cada combustível.

#### Solução em Java

```java
package exercicios;

import java.util.Scanner;

public class Combustivel {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int alcool = 0;
        int gasolina = 0;
        int diesel = 0;

        System.out.print("Informe um código (1, 2, 3) ou 4 para parar: ");
        int codigo = sc.nextInt();

        while (codigo != 4) {
            switch (codigo) {
                case 1:
                    alcool++;
                    break;
                case 2:
                    gasolina++;
                    break;
                case 3:
                    diesel++;
                    break;
            }
            System.out.print("Informe um código (1, 2, 3) ou 4 para parar: ");
            codigo = sc.nextInt();
        }

        System.out.println("MUITO OBRIGADO");
        System.out.println("Alcool: " + alcool);
        System.out.println("Gasolina: " + gasolina);
        System.out.println("Diesel: " + diesel);

        sc.close();
    }
}
```

#### Exemplo de Execução

```
Informe um código (1, 2, 3) ou 4 para parar: 8
Informe um código (1, 2, 3) ou 4 para parar: 1
Informe um código (1, 2, 3) ou 4 para parar: 7
Informe um código (1, 2, 3) ou 4 para parar: 2
Informe um código (1, 2, 3) ou 4 para parar: 2
Informe um código (1, 2, 3) ou 4 para parar: 4
MUITO OBRIGADO
Alcool: 1
Gasolina: 2
Diesel: 0
```

## Parte 2: Estrutura `for`

A estrutura `for` é ideal para situações em que sabemos exatamente quantas vezes um bloco de código deve ser repetido, como ao percorrer um vetor ou executar uma tarefa um número fixo de vezes.

### 1\. Problema "tabuada"

**Descrição:** Ler um número inteiro N e mostrar na tela a tabuada de N de 1 a 10.

#### Solução em Java

```java
package exercicios;

import java.util.Scanner;

public class Tabuada {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Deseja a tabuada para qual valor? ");
        int n = sc.nextInt();

        for (int i = 1; i <= 10; i++) {
            int resultado = n * i;
            System.out.printf("%d x %d = %d\n", n, i, resultado);
        }
        sc.close();
    }
}
```

#### Exemplo de Execução

```
Deseja a tabuada para qual valor? 4
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40
```

### 2\. Problema "soma\_impares"

**Descrição:** Leia 2 valores inteiros X e Y em qualquer ordem. Calcule e mostre a soma dos números ímpares *entre* eles.

#### Solução em Java

```java
package exercicios;

import java.util.Scanner;

public class SomaImpares {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite dois números:");
        int x = sc.nextInt();
        int y = sc.nextInt();
        
        // Garante que x seja o menor e y o maior
        if (x > y) {
            int troca = x;
            x = y;
            y = troca;
        }

        int soma = 0;
        for (int i = x + 1; i < y; i++) {
            if (i % 2 != 0) {
                soma += i;
            }
        }

        System.out.println("SOMA DOS IMPARES = " + soma);
        sc.close();
    }
}
```

#### Exemplo de Execução

```
Digite dois numeros:
6
-5
SOMA DOS IMPARES = 5
```

### 3\. Problema "dentro\_fora"

**Descrição:** Leia um valor inteiro N, que indica a quantidade de valores inteiros X que serão lidos a seguir. Mostre quantos desses valores X estão dentro do intervalo [10, 20] e quantos estão fora.

#### Solução em Java

```java
package exercicios;

import java.util.Scanner;

public class DentroFora {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Quantos números você vai digitar? ");
        int n = sc.nextInt();
        
        int dentro = 0;
        int fora = 0;

        for (int i = 0; i < n; i++) {
            System.out.print("Digite um número: ");
            int x = sc.nextInt();
            if (x >= 10 && x <= 20) {
                dentro++;
            } else {
                fora++;
            }
        }

        System.out.println(dentro + " DENTRO");
        System.out.println(fora + " FORA");

        sc.close();
    }
}
```

#### Exemplo de Execução

```
Quantos números você vai digitar? 5
Digite um número: 14
Digite um número: 35
Digite um número: 10
Digite um número: 131
Digite um número: 8
2 DENTRO
3 FORA
```

### 4\. Problema "divisao"

**Descrição:** Escreva um algoritmo que leia dois números e imprima o resultado da divisão do primeiro pelo segundo. Caso não seja possível (divisão por zero), mostre a mensagem "DIVISAO IMPOSSIVEL". O programa deve fazer isso N vezes, conforme um número de casos informado inicialmente.

#### Solução em Java

```java
package exercicios;

import java.util.Locale;
import java.util.Scanner;

public class Divisao {

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Quantos casos você vai digitar? ");
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            System.out.print("Entre com o numerador: ");
            int numerador = sc.nextInt();
            System.out.print("Entre com o denominador: ");
            int denominador = sc.nextInt();

            if (denominador == 0) {
                System.out.println("DIVISAO IMPOSSIVEL");
            } else {
                double resultado = (double) numerador / denominador;
                System.out.printf("DIVISAO = %.2f\n", resultado);
            }
        }
        sc.close();
    }
}
```

#### Exemplo de Execução

```
Quantos casos você vai digitar? 3
Entre com o numerador: 3
Entre com o denominador: -2
DIVISAO = -1.50
Entre com o numerador: -8
Entre com o denominador: 0
DIVISAO IMPOSSIVEL
Entre com o numerador: 0
Entre com o denominador: 8
DIVISAO = 0.00
```

### 5\. Problema "fatorial"

**Descrição:** Fazer um programa para ler um número natural N (valor máximo: 15) e depois calcular e mostrar o fatorial de N.

#### Solução em Java

```java
package exercicios;

import java.util.Scanner;

public class Fatorial {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o valor de N: ");
        int n = sc.nextInt();
        
        long fatorial = 1; // Usar long para suportar fatoriais maiores

        // Fatorial de 0 é 1 por definição
        for (int i = 1; i <= n; i++) {
            fatorial *= i;
        }

        System.out.println("FATORIAL = " + fatorial);
        sc.close();
    }
}
```

#### Exemplo de Execução

```
Digite o valor de N: 6
FATORIAL = 720
```

### 6\. Problema "experiencias"

**Descrição:** Maria, estudante de medicina, precisa organizar os dados de experimentos de um laboratório. Ela quer saber o total de cobaias utilizadas e o percentual de cada tipo (sapos, ratos, coelhos). O programa deve ler um inteiro N (número de experimentos). Cada experimento tem a quantidade de cobaias e o tipo ('C', 'R' ou 'S'). Ao final, deve apresentar um relatório completo.

#### Solução em Java

```java
package exercicios;

import java.util.Locale;
import java.util.Scanner;

public class Experiencias {

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Quantos casos de teste serão digitados? ");
        int n = sc.nextInt();

        int totalCoelhos = 0;
        int totalRatos = 0;
        int totalSapos = 0;

        for (int i = 0; i < n; i++) {
            System.out.print("Quantidade de cobaias: ");
            int quantidade = sc.nextInt();
            System.out.print("Tipo de cobaia (C, R, S): ");
            char tipo = sc.next().charAt(0);

            switch (Character.toUpperCase(tipo)) {
                case 'C':
                    totalCoelhos += quantidade;
                    break;
                case 'R':
                    totalRatos += quantidade;
                    break;
                case 'S':
                    totalSapos += quantidade;
                    break;
            }
        }

        int totalCobaias = totalCoelhos + totalRatos + totalSapos;
        double percentualCoelhos = ((double) totalCoelhos / totalCobaias) * 100.0;
        double percentualRatos = ((double) totalRatos / totalCobaias) * 100.0;
        double percentualSapos = ((double) totalSapos / totalCobaias) * 100.0;

        System.out.println("\nRELATÓRIO FINAL:");
        System.out.println("Total: " + totalCobaias + " cobaias");
        System.out.println("Total de coelhos: " + totalCoelhos);
        System.out.println("Total de ratos: " + totalRatos);
        System.out.println("Total de sapos: " + totalSapos);
        System.out.printf("Percentual de coelhos: %.2f%%\n", percentualCoelhos);
        System.out.printf("Percentual de ratos: %.2f%%\n", percentualRatos);
        System.out.printf("Percentual de sapos: %.2f%%\n", percentualSapos);
        
        sc.close();
    }
}
```

#### Exemplo de Execução

```
Quantos casos de teste serão digitados? 10
Quantidade de cobaias: 10
Tipo de cobaia (C, R, S): C
Quantidade de cobaias: 6
Tipo de cobaia (C, R, S): R
Quantidade de cobaias: 15
Tipo de cobaia (C, R, S): S
Quantidade de cobaias: 5
Tipo de cobaia (C, R, S): C
Quantidade de cobaias: 14
Tipo de cobaia (C, R, S): R
Quantidade de cobaias: 9
Tipo de cobaia (C, R, S): C
Quantidade de cobaias: 6
Tipo de cobaia (C, R, S): R
Quantidade de cobaias: 8
Tipo de cobaia (C, R, S): S
Quantidade de cobaias: 5
Tipo de cobaia (C, R, S): C
Quantidade de cobaias: 14
Tipo de cobaia (C, R, S): R

RELATÓRIO FINAL:
Total: 92 cobaias
Total de coelhos: 29
Total de ratos: 40
Total de sapos: 23
Percentual de coelhos: 31.52%
Percentual de ratos: 43.48%
Percentual de sapos: 25.00%
```

---

### [ricardotecpro.github.io](https://ricardotecpro.github.io/)

