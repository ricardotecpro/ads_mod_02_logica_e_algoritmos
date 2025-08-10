# 📜 Capítulo 2: Introdução à Programação

Neste capítulo, exploramos os conceitos fundamentais que formam a base da programação de computadores, desde a ideia de um algoritmo até as ferramentas que usamos para construir software.

## 🤖 Algoritmo, Automação e Programas de Computador

### O que é um Algoritmo?

Um **algoritmo** é uma sequência finita e bem definida de instruções com o objetivo de resolver um problema. Embora o termo seja central na computação, ele se aplica a diversas outras áreas do conhecimento.

> **Exemplo Prático: Lavar Roupa**
>
> 1.  Colocar a roupa em um recipiente.
> 2.  Adicionar sabão e amaciante.
> 3.  Encher o recipiente com água.
> 4.  Mexer para dissolver o sabão.
> 5.  Deixar de molho por vinte minutos.
> 6.  Esfregar a roupa.
> 7.  Enxaguar.
> 8.  Torcer para remover o excesso de água.

### O que é Automação?

**Automação** é o processo de usar uma máquina para executar um procedimento de forma automática ou semiautomática. O computador, por exemplo, é uma máquina projetada para automatizar a execução de algoritmos.

### Relação com Computadores

Um computador é formado por duas partes principais:

  * **Hardware**: A parte física (a máquina e seus componentes).
  * **Software**: A parte lógica (os programas, como sistema operacional, aplicativos e jogos).

Nesse contexto, um **programa de computador** é, em linhas gerais, um algoritmo escrito de forma que o computador consiga executá-lo. No entanto, o computador não executa qualquer tipo de algoritmo, mas sim **algoritmos computacionais**, que envolvem principalmente processamento de dados e cálculos.

## 🛠️ O que é preciso para criar um programa?

Para desenvolver um programa de computador, precisamos de um conjunto de ferramentas:

1.  Uma **Linguagem de Programação**: Define as regras para escrever o código.
2.  Uma **IDE (Ambiente de Desenvolvimento Integrado)**: Um software que facilita a edição e o teste do programa.
3.  Um **Compilador** ou **Interpretador**: Um programa que transforma nosso código em algo que a máquina possa executar.

### 1\. Linguagem de Programação

É um conjunto de regras **léxicas** (ortografia das palavras) e **sintáticas** (gramática das frases) usado para escrever programas.

  * **Léxica**: Refere-se à grafia correta das palavras reservadas e identificadores da linguagem.
      * *Exemplo*: `main` está correto, enquanto `maim` está incorreto.
  * **Sintática**: Refere-se à organização correta das palavras para formar instruções válidas.
      * *Exemplo*: `x = 2 + y;` é uma sentença sintaticamente correta.

Existem muitas linguagens de programação, como C, C++, Java, C\#, Python, Ruby, PHP, JavaScript, entre outras.

#### Exemplo Prático: Média de Dois Números

Vamos criar um programa que solicita ao usuário dois números e exibe a média aritmética deles.

**Saída Esperada:**

```
Digite o primeiro numero: 8
Digite o segundo numero: 5
Media = 6.5
```

-----

**Solução em Linguagem C**

```c
#include <stdio.h>

int main() {
    double x, y, media;

    printf("Digite o primeiro numero: ");
    scanf("%lf", &x);

    printf("Digite o segundo numero: ");
    scanf("%lf", &y);

    media = (x + y) / 2.0;
    printf("Media = %.1f\n", media);

    return 0;
}
```

-----

**Solução em Linguagem C++**

```cpp
#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    double x, y, media;

    cout << "Digite o primeiro numero: ";
    cin >> x;

    cout << "Digite o segundo numero: ";
    cin >> y;

    media = (x + y) / 2.0;
    cout << fixed << setprecision(1);
    cout << "Media = " << media << endl;

    return 0;
}
```

-----

**Solução em Linguagem Java (Adaptada para VS Code / IntelliJ IDEA)**

  * **Identificadores Traduzidos**: A classe `Main` foi renomeada para `Programa` para melhor legibilidade em português.

<!-- end list -->

```java
import java.util.Locale;
import java.util.Scanner;

// A classe foi renomeada de "Main" para "Programa"
public class Programa {

    // O método "main" deve ser mantido com este nome
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner leitor = new Scanner(System.in);

        double x, y, media;

        // As mensagens para o usuário estão em português
        System.out.print("Digite o primeiro numero: ");
        x = leitor.nextDouble();

        System.out.print("Digite o segundo numero: ");
        y = leitor.nextDouble();

        media = (x + y) / 2.0;
        System.out.printf("Media = %.1f\n", media);

        leitor.close();
    }
}
```

-----

**Solução em Linguagem C\#**

```csharp
using System;
using System.Globalization;

namespace Curso {
    class Programa {
        static void Main(string[] args) {

            double x, y, media;

            Console.Write("Digite o primeiro numero: ");
            x = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

            Console.Write("Digite o segundo numero: ");
            y = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

            media = (x + y) / 2.0;
            Console.WriteLine("Media = " + media.ToString("F1", CultureInfo.InvariantCulture));
        }
    }
}
```

### 2\. IDE (Ambiente de Desenvolvimento Integrado)

Uma **IDE** é um software que agrupa ferramentas para auxiliar na construção de programas. IDEs modernas como **VS Code**, **IntelliJ IDEA** e **Visual Studio** são amplamente utilizadas no mercado.

**Exemplos de IDEs por linguagem:**

  * **C/C++**: Code::Blocks, VS Code com extensões C/C++.
  * **Java**: IntelliJ IDEA, Eclipse, VS Code com Extension Pack for Java.
  * **C\#**: Microsoft Visual Studio, VS Code com C\# Dev Kit.

**Funcionalidades comuns de uma IDE:**

  * Editor de código avançado (autocompletar, destaque de sintaxe).
  * Ferramentas de depuração (`debugger`) e testes.
  * Automação de compilação e construção (`build`) do projeto.

### 3\. Compilação e Interpretação

O **código-fonte** é o código que o programador escreve na linguagem de programação. Para que o computador o execute, ele precisa passar por um processo de tradução. Existem três abordagens principais:

1.  **Compilação**: O `Compilador` analisa o código-fonte e o traduz para um **código-objeto**. Em seguida, um `Gerador de código` cria um **código executável** específico para o sistema operacional.

      * **Linguagens**: C, C++.
      * **Vantagens**: Maior velocidade de execução e verificação de erros antes da execução.

2.  **Interpretação**: O `Interpretador` analisa e executa o código-fonte instrução por instrução, sob demanda, sem gerar um arquivo executável separado.

      * **Linguagens**: PHP, JavaScript, Python, Ruby.
      * **Vantagens**: Maior flexibilidade (o código não precisa ser recompilado para diferentes plataformas) e expressividade.

3.  **Abordagem Híbrida**: O código-fonte é pré-compilado para um código intermediário chamado **bytecode**. Esse bytecode é então interpretado por uma **Máquina Virtual** (VM), que o traduz para os comandos nativos da máquina onde está sendo executado.

      * **Linguagens**: Java (com a JVM), C\# (com o .NET Framework).
      * **Vantagem**: Combina a portabilidade da interpretação com um desempenho otimizado, próximo ao da compilação.

## ✍️ A Linguagem "Portugol" e o VisualG

### O que é "Portugol"?

"Portugol" é um pseudocódigo com regras em português, criado com fins didáticos para ensinar lógica de programação a estudantes de língua portuguesa. O seu principal objetivo é permitir que o aluno se concentre em aprender a **lógica** (como resolver o problema), sem se preocupar com as complexidades da sintaxe de uma linguagem de programação real.

É importante notar que o "Portugol" não é uma linguagem formal e pode ter pequenas variações de sintaxe entre diferentes autores, sendo chamado também de "Português Estruturado".

### O que é o VisualG?

**VisualG** é uma IDE simples usada para escrever, interpretar e testar algoritmos em um dos dialetos do Portugol. Ele serve como uma ferramenta prática para aplicar os conceitos de lógica de programação.

#### Exemplo: "Olá, Mundo\!" em Portugol com VisualG

Este é um exemplo de um primeiro algoritmo escrito na sintaxe do VisualG.

```
algoritmo "primeiro"
// Esta seção é usada para declarar variáveis
var

inicio
// Esta seção contém os comandos do algoritmo
   escreva("Ola mundo!")

fimalgoritmo
```