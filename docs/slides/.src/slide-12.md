# Aula 12 - Ecossistema C# e .NET 🔷

---

## Agenda 📅

1.  O Que é .NET? { .fragment }
2.  Ferramentas (VS vs VS Code) { .fragment }
3.  C# Básico { .fragment }
4.  LINQ (A Mágica) { .fragment }
5.  F# (O Lado Funcional) { .fragment }

---

## 1. O Que é .NET? 🏗️

- **C#**: A Linguagem. { .fragment }
- **.NET**: A Plataforma (Runtime, Bibliotecas). { .fragment }
- Criado pela Microsoft para bater de frente com o Java. { .fragment }
- Hoje é **Open Source** e roda no Linux/Mac. { .fragment }

---

## 2. Ferramentas 🛠️

Onde programar?

- **Visual Studio (Roxo)**: A IDE completa. Pesada. Faz tudo (Arrastar botões, Banco de Dados). { .fragment }
- **VS Code (Azul)**: Editor leve. Rápido. Exige instalar extensões. { .fragment }

---

### Criando um Projeto 💻

No terminal:

1.  `dotnet new console -o MeuApp` { .fragment }
2.  `cd MeuApp` { .fragment }
3.  `code .` { .fragment }
4.  `dotnet run` { .fragment }

---

## 3. C# Básico 📝

Muito parecido com Java.

```csharp
using System;

class Program {
    static void Main() {
        Console.WriteLine("Olá, C#!");
        // Em Java seria System.out.println
    }
}
```

---

## 4. LINQ: A Joia da Coroa 💎

**L**anguage **In**tegrated **Q**uery.

- Tratar listas como se fossem SQL. { .fragment }
- Filtrar, Ordenar, Transformar dados em **uma linha**. { .fragment }

---

### Sem LINQ (Jeito Velho) 👴

```csharp
List<int> pares = new List<int>();
foreach (int n in numeros) {
    if (n % 2 == 0) {
        pares.Add(n);
    }
}
```

---

### Com LINQ (Jeito Novo) ✨

```csharp
var pares = numeros.Where(n => n % 2 == 0).ToList();
```

> Muito mais limpo e legível!

---

### Visualizando LINQ (Mermaid)

```mermaid
graph LR;
    Input[Lista: 1, 2, 3, 4] -->|Where| Filtro[Pares: 2, 4];
    Filtro -->|Select| Transf[Quadrado: 4, 16];
    Transf --> Output[Resultado];
```

---

## Tipos de Dados Poderosos 💪

- **var**: O compilador adivinha o tipo. { .fragment }
    - `var x = 10;` (Vira int). { .fragment }
- **Nullable Types**: { .fragment }
    - `int? idade = null;` (Pode ser nulo). { .fragment }
    - Evita erros de memória. { .fragment }

---

## 5. F# (Bônus) 🟣

- Linguagem **Funcional** do .NET. { .fragment }
- Focada em Matemática e Dados. { .fragment }
- Influenciou o LINQ e as Lambdas do C#. { .fragment }
- Código muito conciso. { .fragment }

---

## Exercício Rápido ⚡

**LINQ na Prática**

Dada uma lista de preços: `[10.5, 20.0, 5.0, 100.0]`

1.  Filtre os preços maiores que 15.0. { .fragment }
2.  Ordene do maior para o menor. { .fragment }
3.  Mostre o resultado. { .fragment }

---

## Resumo ✅

- C# é moderno, forte e produtivo. { .fragment }
- **.NET** roda em tudo. { .fragment }
- **LINQ** salva vidas (e linhas de código). { .fragment }
- Visual Studio é a casa do C#. { .fragment }

---

## Próxima Aula 🚀

- Vamos sair das linguagens compiladas. { .fragment }
- Vamos para a linguagem mais popular da Ciência de Dados. { .fragment }
- **Python**: Simples, poderoso e lento (mas ninguém liga). { .fragment }

👉 **Tarefa**: Instalar o .NET SDK!