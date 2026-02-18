# Aula 01 - Conteúdo do Curso

Este documento apresenta a estrutura completa do curso de formação em algoritmos e desenvolvimento de software.

```bash
$ echo "Bem-vindo ao curso de Lógica!"
Bem-vindo ao curso de Lógica!
```
{: .termy }

## 📚 Conteúdo do Curso

O curso é dividido em duas grandes áreas: a base de lógica de programação com Portugol e a aplicação desses conceitos em linguagens de programação populares no mercado.

### **Algoritmos e Lógica de Programação (Portugol e VisualG)**

Nesta primeira parte, o foco é construir uma base sólida em lógica, essencial para qualquer desenvolvedor.

1.  **Apresentação do curso**: Objetivos, metodologia e visão geral do conteúdo.
2.  **Conceitos de programação**: O que são algoritmos, variáveis, tipos de dados e operadores.
3.  **Estrutura sequencial**: Execução de comandos passo a passo.
4.  **Estrutura condicional**: Uso de `se-entao-senao` para criar fluxos de decisão.
5.  **Estruturas repetitivas**: Comandos de repetição como `enquanto`, `para` e `repita-ate`.
6.  **Vetores**: Manipulação de listas de dados unidimensionais.
7.  **Matrizes**: Trabalho com tabelas e estruturas de dados bidimensionais.

### **Linguagens de Programação**

Com a base lógica consolidada, o curso avança para a implementação em linguagens modernas.

8.  **Instalação das ferramentas**: Configuração de ambientes de desenvolvimento como VS Code, IntelliJ IDEA, PyCharm e outros.
9.  **Linguagem C**: Uma linguagem estruturada fundamental para entender o funcionamento de baixo nível.
10. **Linguagem C++**: Evolução do C com suporte à programação orientada a objetos.
11. **Linguagem Java**: Foco em portabilidade e orientação a objetos para sistemas robustos.
12. **Linguagem C#**: A solução da Microsoft para desenvolvimento de aplicações web, desktop e jogos.
13. **Linguagem Python**: Sintaxe limpa e ecossistema rico para ciência de dados, web e automação.

## 🚀 Percurso de Formação

O percurso de aprendizado foi desenhado para garantir uma progressão lógica e consistente, do teórico ao prático.

1.  **Fundamentos**: Inicia-se com o estudo de **Algoritmos e Lógica de Programação** (Capítulos 1 a 7), construindo a base do pensamento computacional.
2.  **Configuração do Ambiente**: Em seguida, realiza-se a **instalação das ferramentas de desenvolvimento** (Capítulo 8), como VS Code, PyCharm, IntelliJ IDEA e Visual Studio.
3.  **Aplicação Prática**: Por fim, o aluno pode escolher ou seguir a sequência de linguagens para aplicar os conhecimentos adquiridos:
    - **Linguagem C** (Capítulo 9)
    - **Linguagem C++** (Capítulo 10)
    - **Linguagem Java** (Capítulo 11)
    - **Linguagem C#** (Capítulo 12)
    - **Linguagem Python** (Capítulo 13)

---

## **📚 Curso de Scratch para Logística/Administração**:

* 📌 **Emojis** para facilitar leitura e deixar mais leve.
* 💡 **Exemplos práticos** usando **extensões do Scratch** (sensores, tradutor, texto-para-fala, etc.).
* 📊 **Diagramas** em formatos compatíveis com JetBrains (Mermaid, PlantUML, Draw\.io, Excalidraw).
* 🔗 Links e ideias de integração para os alunos criarem fluxos antes de programar.

---

## **📚 Curso: Programando com Scratch para Logística e Administração**

**⏳ Carga horária sugerida:** 20h (5 encontros de 4h ou 10 encontros de 2h)
**🎯 Objetivo:** Ensinar programação e pensamento computacional com **Scratch**, aplicando em **processos logísticos** e **gestão administrativa**.

---

## **🧩 Módulo 1 – Introdução ao Scratch e à Lógica de Programação** (2h)

**Objetivos:**

* Apresentar o Scratch e conceitos básicos de programação.
* Mostrar a relação entre **automação** e **gestão de processos**.

**Conteúdo:**

* O que é Scratch e como acessar (online/offline).
* Interface e blocos básicos.
* Pensamento computacional na logística/administração.

**Extensões usadas:**

* 🎤 Texto para fala (Text-to-Speech) para criar mensagens automáticas.

**Atividade prática:**

* Criar um **atendente virtual** que dá boas-vindas ao cliente.

**Diagrama de exemplo (Mermaid)**

```mermaid
flowchart TD
    A[Cliente chega] --> B[Mensagem de boas-vindas]
    B --> C[Oferecer menu de serviços]
    C --> D[Fim]
```

---

## **⚙ Módulo 2 – Sequências, Eventos e Controle** (4h)

**Objetivos:**

* Criar sequências de ações e reações a eventos.
* Usar estruturas de controle.

**Conteúdo:**

* Blocos de eventos ("quando clicar", "quando tecla pressionada").
* Controle: **esperar**, **repetir**, **se...então**.

**Extensões usadas:**

* ⏱ Cronômetro para medir tempo de atendimento.

**Atividade prática:**

* **Projeto:** Simulador de atendimento em fila, calculando tempo de espera.

**Diagrama de exemplo (PlantUML)**

```plantuml
@startuml
start
:Cliente entra na fila;
:Inicia cronômetro;
if (Atendimento disponível?) then (Sim)
  :Atender cliente;
else (Não)
  :Esperar;
endif
stop
@enduml
```
**Diagrama de exemplo (Mermaid)**

```mermaid

flowchart TD
    A[Cliente entra na fila] --> B[Inicia cronômetro]
    B --> C{Atendimento disponível?}
    C -->|Sim| D[Atender cliente]
    C -->|Não| E[Esperar]
    D --> F[Fim]
    E --> F
```


---

## **📊 Módulo 3 – Variáveis, Operadores e Entrada de Dados** (4h)

**Objetivos:**

* Trabalhar com variáveis e operadores matemáticos/lógicos.

**Conteúdo:**

* Criando variáveis para armazenar valores.
* Operadores para cálculos de custo e prazos.

**Extensões usadas:**

* 📦 Tradutor para oferecer atendimento em múltiplos idiomas.

**Atividade prática:**

* **Projeto:** Calculadora de frete (peso × distância).

**Fluxo em Draw\.io (pseudocódigo gráfico)**
*(O professor pode abrir no JetBrains usando plugin Draw\.io Integration)*

---

## **📋 Módulo 4 – Listas e Tomada de Decisão** (4h)

**Objetivos:**

* Criar e manipular listas.
* Tomar decisões com base em dados armazenados.

**Conteúdo:**

* Adicionar, remover, buscar itens em listas.
* Filtrar informações.

**Extensões usadas:**

* 📡 Sensor de vídeo (simular scanner de código de barras).

**Atividade prática:**

* **Projeto:** Controle de estoque com consulta de produtos.

**Exemplo em Excalidraw:**

* Fluxo de cadastro/consulta/remoção de item.

---

## **🚚 Módulo 5 – Funções, Modularização e Projeto Final** (6h)

**Objetivos:**

* Criar blocos personalizados para modular o código.
* Desenvolver um sistema mais completo.

**Conteúdo:**

* Funções (blocos definidos pelo usuário).
* Reuso de código e integração de recursos.

**Extensões usadas:**

* 🗓 Data e hora para agendamento de entregas.

**Atividade prática:**

* **Projeto final:** Sistema de agendamento de entregas.

**Fluxo em Mermaid (entrega de pedidos)**

```mermaid
flowchart LR
    A[Receber pedido] --> B[Agendar data/hora]
    B --> C[Calcular rota]
    C --> D[Registrar no sistema]
    D --> E[Gerar relatório]
```

---

## **📌 Estratégias e melhorias**

1. **Usar sempre exemplos do mundo real** da logística/administração.
2. **Diagramar antes de programar** usando **Mermaid, PlantUML, Draw\.io e Excalidraw** para visualizar fluxos.
3. **Aplicar extensões do Scratch** para simular funções reais (tradutor, sensores, voz).
4. **Projetos progressivos**: cada módulo aproveita o anterior.

---

Se quiser, posso já criar **os arquivos `.sb3` do Scratch** com todos esses projetos, **mais** os diagramas prontos em **.puml, .drawio, .excalidraw** para você abrir direto no JetBrains.

Quer que eu já gere esse pacote completo?

---

### [ricardotecpro.github.io](https://ricardotecpro.github.io/)

---

### 🚀 [ricardotecpro.github.io](https://ricardotecpro.github.io/)

## 🎓 Introdução à Programação

Este guia aborda os conceitos fundamentais da programação, desde a definição de um algoritmo até as ferramentas necessárias para criar seu primeiro programa.

## 🤖 Algoritmo, Automação e Programas

### O que é um Algoritmo? 🤔

Um **algoritmo** é uma **sequência finita e lógica de instruções** para resolver um problema específico. Embora o termo seja muito comum em computação, ele se aplica a diversas outras áreas do conhecimento.

Pense em uma receita de bolo 🎂: ela é um algoritmo. Você segue passos definidos (`misturar ingredientes`, `assar por 30 minutos`) para chegar a um resultado esperado.

**Exemplo prático: Lavar roupa 🧺**

Para o problema "lavar roupa suja", um algoritmo simples seria:

1.  Colocar a roupa em um recipiente (como uma máquina de lavar).
2.  Adicionar sabão e amaciante.
3.  Encher com água.
4.  Deixar de molho por 20 minutos.
5.  Esfregar a roupa (ou deixar a máquina fazer isso).
6.  Enxaguar para remover o sabão.
7.  Torcer para retirar o excesso de água.


```mermaid
graph TD
    A[Início: Roupa Suja] --> B{Colocar na Máquina};
    B --> C[Adicionar Sabão/Amaciante];
    C --> D[Encher com Água];
    
    D --> E["Deixar de Molho (20 min)"];
    E --> F["Esfregar/Lavar (Máquina)"];
    F --> G[Enxaguar];
    G --> H[Torcer];
    H --> I[Estender no Varal];
    I --> J[Recolher Roupa Seca];
    J --> K[Dobrar e Guardar];
    K --> L[Fim: Roupa Limpa];
```    

### O que é Automação? ⚙️

**Automação** é o processo de usar máquinas para executar as tarefas de um algoritmo de forma automática ou semiautomática. Usar uma máquina de lavar, por exemplo, automatiza quase todo o algoritmo de lavar roupas.

### A Relação com Computadores 💻

O computador é a principal ferramenta de automação para o processamento de informações. Ele é composto por duas partes:

  * **Hardware**: A parte física, ou seja, a máquina em si (processador, memória, tela, teclado).
  * **Software**: A parte lógica, que são os programas e dados, incluindo o Sistema Operacional e os aplicativos.

> **Um programa de computador é um algoritmo escrito de forma que o computador consiga entender e executar, automatizando a solução de um problema.**

Contudo, computadores são especializados em **algoritmos computacionais**, que envolvem principalmente o **processamento de dados** e **cálculos matemáticos**.

## 🛠️ Ferramentas Essenciais para Programar

Para criar um programa de computador, você precisará de algumas ferramentas básicas:

1.  **Linguagem de Programação**: Um conjunto de regras para escrever as instruções que o computador seguirá.
2.  **IDE (Ambiente de Desenvolvimento Integrado)**: Um software que facilita a escrita, o teste e a depuração do código.
3.  **Compilador ou Interpretador**: Um programa que "traduz" seu código para a linguagem que a máquina entende.

-----

## 📜 Linguagens de Programação

Uma linguagem de programação possui regras **léxicas** (ortografia das palavras) e **sintáticas** (gramática das frases).

  * **Léxica**: Refere-se à grafia correta das palavras. Exemplo: `main` está correto, `maim` está incorreto.
  * **Sintática**: Refere-se à organização correta das palavras. Exemplo: `x = 10 + y;` está correto, `x = + 10 y;` está incorreto.

Existem muitas linguagens populares, como: **C, C++, Java, C\#, Python, Ruby, PHP e JavaScript**.

### 📝 Exemplo 1: Média de Notas

Este programa solicita o nome e duas notas de um aluno e, em seguida, calcula e exibe a média.

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

#### Solução em Linguagem Java ☕

```java
import java.util.Locale;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        String nome;
        double nota1, nota2, media;

        System.out.print("Digite o nome do aluno: ");
        nome = sc.nextLine();

        System.out.print("Digite a primeira nota: ");
        nota1 = sc.nextDouble();

        System.out.print("Digite a segunda nota: ");
        nota2 = sc.nextDouble();

        media = (nota1 + nota2) / 2.0;

        System.out.printf("A média do(a) aluno(a) %s é: %.2f\n", nome, media);

        sc.close();
    }
}
```

### 📝 Exemplo 2: Área de um Retângulo

Este programa calcula a área de um retângulo com base nos valores de base e altura fornecidos.

#### Solução em Linguagem C++

```cpp
#include <iostream>
#include <iomanip>

int main() {
    double base, altura, area;

    std::cout << "Digite o valor da base: ";
    std::cin >> base;

    std::cout << "Digite o valor da altura: ";
    std::cin >> altura;

    area = base * altura;

    std::cout << "A área do retângulo é: " << std::fixed << std::setprecision(2) << area << std::endl;

    return 0;
}
```

**Saída Esperada:**

```
Digite o valor da base: 10.0
Digite o valor da altura: 5.0
A área do retângulo é: 50.00
```

#### Solução em Linguagem C\# 💎

```csharp
using System;
using System.Globalization;

namespace Curso {
    class Programa {
        static void Main(string[] args) {
            double baseRet, altura, area;

            Console.Write("Digite o valor da base: ");
            baseRet = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

            Console.Write("Digite o valor da altura: ");
            altura = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

            area = baseRet * altura;

            Console.WriteLine("A área do retângulo é: " + area.ToString("F2", CultureInfo.InvariantCulture));
        }
    }
}
```

**Saída Esperada:**

```
Digite o valor da base: 10.0
Digite o valor da altura: 5.0
A área do retângulo é: 50.00
```

## 💻 IDEs (Ambientes de Desenvolvimento Integrado)

Uma **IDE** é um programa que reúne diversas ferramentas para facilitar a vida do desenvolvedor. Funcionalidades comuns incluem edição de código avançada, depuração (`debugging`) e automação de compilação.

**IDEs Populares por Linguagem:**

  * **Java**: **IntelliJ IDEA** e **VS Code** (com o *Extension Pack for Java*).
  * **C\#**: **Microsoft Visual Studio** e **VS Code** (com a extensão C\#).
  * **C/C++**: **VS Code** (com extensões C/C++) e **CLion**.

## ⚙️ Compilação vs. Interpretação

Para que um computador execute um programa, o **código-fonte** (o que você escreve) precisa ser traduzido. Existem três abordagens principais:

### 1\. Compilação

Um **Compilador** traduz todo o código-fonte de uma vez, gerando um **código executável**.

  * **Vantagens**: Execução muito rápida 🚀.
  * **Linguagens Típicas**: **C**, **C++**.

### 2\. Interpretação

Um **Interpretador** lê e executa o código-fonte linha por linha.

  * **Vantagens**: Mais flexível, o mesmo código roda em qualquer plataforma 🌐.
  * **Linguagens Típicas**: **PHP**, **JavaScript**, **Python**, **Ruby**.

### 3\. Abordagem Híbrida

O código-fonte é pré-compilado para um código intermediário chamado **Bytecode**, que é então interpretado por uma **Máquina Virtual (VM)**.

  * **Vantagens**: Portabilidade e bom desempenho.
  * **Linguagens Típicas**: **Java** (com a JVM), **C\#** (com o .NET).

## Portugol e Ferramentas de Aprendizagem

Para focar no aprendizado da **lógica do algoritmo** sem a complexidade de uma linguagem real, utiliza-se o **Portugol**. É uma pseudo-linguagem didática com sintaxe simplificada e em português.

**Atenção**: Portugol é uma linguagem para aprender, não para criar programas comerciais.

Existem IDEs simples para escrever e testar algoritmos em Portugol:

  * **VisualG**: Uma ferramenta clássica e leve.
  * **Portugol Studio**: Uma alternativa mais moderna e com mais recursos. Você pode encontrá-lo em `portugol.dev`.

### Exemplo em VisualG

```console
$ visualg
Iniciando VisualG...
```

```visualg
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

As principais diferenças são a estrutura do programa (`programa { ... }`), a declaração de variáveis dentro da função e o operador de atribuição (`=` em vez de `<-`).

### Exemplo em Portugol Studio

```portugol
programa
{
	// A função 'inicio' é o ponto de entrada do programa.
	funcao inicio()
	{
		// Área de declaração de variáveis
		cadeia nome
		real nota1, nota2, media

		// Corpo do algoritmo (Entrada, Processamento e Saída de Dados)
		escreva("Digite o nome do aluno(a): ")
		leia(nome)
		
		escreva("Digite a primeira nota: ")
		leia(nota1)
		
		escreva("Digite a segunda nota: ")
		leia(nota2)
		
		// Processamento: calcula a média
		media = (nota1 + nota2) / 2
		
		// Saída: exibe o resultado formatado
		escreva("\nA média do(a) aluno(a) ", nome, " é: ", media)
	}
}
```

**Principais Mudanças e Explicações:**

1.  **Estrutura:** O Portugol Studio usa uma estrutura de blocos com chaves `{}`. O programa inteiro é envolvido por `programa { ... }`.
2.  **Função Principal:** Todo o código executável deve estar dentro da função `funcao inicio() { ... }`.
3.  **Declaração de Variáveis:** As variáveis são declaradas no início da função onde serão usadas, não em um bloco `var` separado.
4.  **Tipos de Dados:** O tipo `caractere` do VisualG corresponde ao tipo `cadeia` no Portugol Studio. O tipo `real` é o mesmo.
5.  **Atribuição:** O operador para atribuir um valor a uma variável é o sinal de igual (`=`), e não a seta (`<-`).
6.  **Comandos de Escrita:** O comando `escreval` do VisualG é equivalente ao `escreva` do Portugol Studio. Ambos pulam uma linha ao final da escrita. O `\n` foi adicionado na última linha para dar um espaçamento extra antes da mensagem final, tornando a saída mais legível.

---

### 🚀 [ricardotecpro.github.io](https://ricardotecpro.github.io/)
