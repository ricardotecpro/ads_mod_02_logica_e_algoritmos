# 🎓 Introdução à Programação

Este guia aborda os conceitos fundamentais da programação, desde a definição de um algoritmo até as ferramentas necessárias para criar seu primeiro programa.

## 🤖 Algoritmo, Automação e Programas

### O que é um Algoritmo?

Um **algoritmo** é uma **sequência finita e lógica de instruções** para resolver um problema específico. Embora o termo seja muito comum em computação, ele se aplica a diversas outras áreas do conhecimento.

Pense em uma receita de bolo: ela é um algoritmo. Você segue passos definidos (`misturar ingredientes`, `assar por 30 minutos`) para chegar a um resultado esperado (um bolo delicioso).

**Exemplo prático: Lavar roupa**

Para o problema "lavar roupa suja", um algoritmo simples seria:

1.  Colocar a roupa em um recipiente (como uma máquina de lavar).
2.  Adicionar sabão e amaciante.
3.  Encher com água.
4.  Agitar para dissolver os produtos.
5.  Deixar de molho por 20 minutos.
6.  Esfregar a roupa (ou deixar a máquina fazer isso).
7.  Enxaguar para remover o sabão.
8.  Torcer para retirar o excesso de água.

### O que é Automação?

**Automação** é o processo de usar máquinas para executar as tarefas de um algoritmo de forma automática ou semiautomática.

Seguindo o exemplo anterior, usar uma máquina de lavar automatiza quase todo o algoritmo de lavar roupas. Você apenas realiza os primeiros passos, e a máquina cuida do resto.

### A Relação com Computadores

O computador é a principal ferramenta de automação para o processamento de informações. Ele é composto por duas partes:

- **Hardware**: A parte física, ou seja, a máquina em si (processador, memória, tela, teclado).
- **Software**: A parte lógica, que são os programas e dados. Inclui:
    - **Sistema Operacional**: O software base que gerencia o hardware (Windows, Linux, macOS).
    - **Aplicativos**: Programas para tarefas específicas (navegador de internet, editores de texto).
    - **Jogos**, **Utilitários** (antivírus, compactadores) e outros.

Em resumo:

> **Um programa de computador é um algoritmo escrito de forma que o computador consiga entender e executar, automatizando a solução de um problema.**

Contudo, computadores não executam qualquer tipo de algoritmo. Eles são especializados em **algoritmos computacionais**, que envolvem principalmente:

- **Processamento de dados**
- **Cálculos matemáticos**

## 🛠️ Ferramentas Essenciais para Programar

Para criar um programa de computador, você precisará de algumas ferramentas básicas:

1.  **Linguagem de Programação**: Um conjunto de regras para escrever as instruções que o computador seguirá.
2.  **IDE (Ambiente de Desenvolvimento Integrado)**: Um software que facilita a escrita, o teste e a depuração do código.
3.  **Compilador ou Interpretador**: Um programa que "traduz" seu código para a linguagem que a máquina entende.
4.  **Gerador de Código ou Máquina Virtual**: Ferramentas que preparam o programa para ser executado.

-----

## 📜 Linguagens de Programação

Uma linguagem de programação possui regras **léxicas** e **sintáticas**.

### Léxica (Ortografia)

A **léxica** se refere à grafia correta das "palavras" isoladas da linguagem.

| Português | Linguagem de Programação |
| :--- | :--- |
| ✅ `aluno` | ✅ `main` |
| ❌ `alunno` | ❌ `maim` |

### Sintática (Gramática)

A **sintática** se refere à forma correta de organizar as palavras para formar sentenças válidas.

| Português | Linguagem de Programação |
| :--- | :--- |
| ✅ `A aluna está aprovada.` | ✅ `x = 10 + y;` |
| ❌ `Aprovada está aluna a.` | ❌ `x = + 10 y;` |

Existem muitas linguagens de programação, cada uma com suas forças e fraquezas. Algumas das mais populares são: **C, C++, Java, C\#, Python, Ruby, PHP e JavaScript**.

### 📝 Exemplo de Programa: Média de Notas

Vamos criar um programa que solicita o nome e duas notas de um aluno e, em seguida, calcula e exibe a média.

**Entrada de dados:**

```
Digite o nome do aluno: Bia
Digite a primeira nota: 7.5
Digite a segunda nota: 9.0
```

**Saída esperada:**

```
A média da aluna Bia é: 8.25
```

Veja como o mesmo algoritmo é escrito em diferentes linguagens:

#### Solução em Linguagem C

```c
#include <stdio.h>

int main() {
    char nome[50];
    double nota1, nota2, media;

    printf("Digite o nome do aluno: ");
    scanf("%s", nome);

    printf("Digite a primeira nota: ");
    scanf("%lf", &nota1);

    printf("Digite a segunda nota: ");
    scanf("%lf", &nota2);

    media = (nota1 + nota2) / 2.0;

    printf("A média do(a) aluno(a) %s é: %.2f\n", nome, media);

    return 0;
}
```

#### Solução em Linguagem C++

```cpp
#include <iostream>
#include <string>
#include <iomanip>

int main() {
    std::string nome;
    double nota1, nota2, media;

    std::cout << "Digite o nome do aluno: ";
    std::cin >> nome;

    std::cout << "Digite a primeira nota: ";
    std::cin >> nota1;

    std::cout << "Digite o segundo numero: ";
    std::cin >> nota2;

    media = (nota1 + nota2) / 2.0;

    std::cout << "A média do(a) aluno(a) " << nome << " é: " << std::fixed << std::setprecision(2) << media << std::endl;

    return 0;
}
```

#### Solução em Linguagem C\#

```csharp
using System;
using System.Globalization;

namespace Curso {
    class Programa {
        static void Main(string[] args) {
            string nome;
            double nota1, nota2, media;

            Console.Write("Digite o nome do aluno: ");
            nome = Console.ReadLine();

            Console.Write("Digite a primeira nota: ");
            nota1 = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

            Console.Write("Digite a segunda nota: ");
            nota2 = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

            media = (nota1 + nota2) / 2.0;

            Console.WriteLine("A média do(a) aluno(a) " + nome + " é: " + media.ToString("F2", CultureInfo.InvariantCulture));
        }
    }
}
```

#### Solução em Linguagem Java

```java
import java.util.Locale;
import java.util.Scanner;

// A classe foi renomeada para 'Programa'
public class Programa {

    // O método 'main' deve ser mantido
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        // A variável 'sc' foi mantida, mas poderia ser 'leitor'
        Scanner sc = new Scanner(System.in);

        // Variáveis traduzidas
        String nome;
        double nota1, nota2, media;

        // Literais de string traduzidas
        System.out.print("Digite o nome do aluno: ");
        nome = sc.nextLine();

        System.out.print("Digite a primeira nota: ");
        nota1 = sc.nextDouble();

        System.out.print("Digite a segunda nota: ");
        nota2 = sc.nextDouble();

        // O método 'calcularMedia' é um exemplo de nome traduzido
        media = calcularMedia(nota1, nota2);

        System.out.printf("A média do(a) aluno(a) %s é: %.2f\n", nome, media);

        sc.close();
    }

    // Método auxiliar com nome traduzido
    public static double calcularMedia(double n1, double n2) {
        return (n1 + n2) / 2.0;
    }
}
```

## 💻 IDEs (Ambientes de Desenvolvimento Integrado)

Uma **IDE** é um programa que reúne diversas ferramentas para facilitar a vida do desenvolvedor. Pense nela como um editor de texto superpoderoso, feito especialmente para escrever código.

Funcionalidades comuns:

- **Edição de código avançada**: Sugestões para autocompletar, destaque de palavras-chave e formatação automática.
- **Depuração (Debugging)**: Permite executar o código passo a passo para encontrar erros.
- **Automação de compilação**: Facilita o processo de "construir" e executar o programa.
- **Modelos de projeto (Templates)**: Oferece estruturas prontas para iniciar novos projetos.

### IDEs Populares por Linguagem:

- **Java**: **IntelliJ IDEA** e **VS Code** (com o *Extension Pack for Java*).
- **C\#**: **Microsoft Visual Studio** e **VS Code** (com a extensão C\#).
- **C/C++**: **VS Code** (com extensões C/C++) e **CLion**.

## ⚙️ Compilação vs. Interpretação

Para que um computador execute um programa, o **código-fonte** (o que você escreve) precisa ser traduzido para a linguagem de máquina. Existem três abordagens principais para isso:

### 1\. Compilação

Neste modelo, um programa chamado **Compilador** traduz todo o código-fonte de uma só vez, gerando um novo arquivo, o **código executável**, que é específico para um sistema operacional.

- **Processo**: `Código-fonte` → `Compilador` → `Código-objeto` → `Código Executável`
- **Vantagens**: Execução muito rápida, verificação de erros antes da execução.
- **Linguagens Típicas**: **C**, **C++**.

### 2\. Interpretação

Aqui, um programa chamado **Interpretador** lê e executa o código-fonte linha por linha, sob demanda, sem gerar um arquivo executável separado.

- **Processo**: `Código-fonte` → `Interpretador` → `Execução`
- **Vantagens**: Mais flexível, o mesmo código roda em qualquer plataforma que tenha o interpretador.
- **Linguagens Típicas**: **PHP**, **JavaScript**, **Python**, **Ruby**.

### 3\. Abordagem Híbrida

Essa abordagem combina o melhor dos dois mundos. O código-fonte é pré-compilado para um código intermediário chamado **Bytecode**. Esse bytecode não é executável diretamente, mas é interpretado por uma **Máquina Virtual (VM)**, que o traduz para comandos nativos da máquina.

- **Processo**: `Código-fonte` → `Compilador` → `Bytecode` → `Máquina Virtual (Interpretação)` → `Execução`
- **Vantagens**: Portabilidade (o bytecode roda em qualquer VM) e bom desempenho.
- **Linguagens Típicas**: **Java** (com a JVM), **C\#** (com o .NET).

## 🇵🇹 Portugol e VisualG

Para quem está começando, aprender a sintaxe complexa de uma linguagem de programação e a lógica de programação ao mesmo tempo pode ser difícil.

O **Portugol** (ou "Português Estruturado") resolve isso. É uma pseudo-linguagem didática que usa uma sintaxe simplificada e em português para focar no aprendizado da **lógica do algoritmo**.

- **Atenção**: Portugol é uma linguagem para aprender, não para criar programas comerciais.
- **Dialetos**: A sintaxe pode variar um pouco entre diferentes autores e ferramentas.

O **VisualG** é uma IDE simples feita para escrever e interpretar programas em Portugol, sendo uma excelente ferramenta para iniciantes.

### Exemplo em Portugol (usando a sintaxe do VisualG)

Veja o nosso algoritmo de média de notas escrito em Portugol:

```portugol
algoritmo "CalculoMedia"

// Área de declaração de variáveis
var
   nome: caractere
   nota1, nota2, media: real

// Corpo do algoritmo
inicio
   escreval("Digite o nome do aluno: ")
   leia(nome)
   
   escreval("Digite a primeira nota: ")
   leia(nota1)
   
   escreval("Digite a segunda nota: ")
   leia(nota2)
   
   media <- (nota1 + nota2) / 2
   
   escreval("A média do(a) aluno(a) ", nome, " é: ", media)

fimalgoritmo
```