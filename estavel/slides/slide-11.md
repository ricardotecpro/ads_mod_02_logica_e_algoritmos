# Aula 11 - Java e Orientação a Objetos ☕

---

## Agenda 📅

1.  O Mundo dos Objetos
2.  Classes vs Objetos
3.  Java e a JVM
4.  Os 3 Pilares da OO
5.  Spring Boot (Java Moderno)

---

## 1. O Mundo Orientado a Objetos 🌍

Até agora, programamos **Ações** (Funções).
Mas o mundo é feito de **Coisas** (Objetos).

- **Estruturada**: Verbo (Fazer algo).
- **OO**: Substantivo (Algo que faz).

---

## 2. Classe vs Objeto 🏗️

A distinção mais importante.

- **Classe**: O Molde. A Planta. A Ideia. (Abstrato).
- **Objeto**: A Instância. A Casa. A Coisa Real. (Concreto).

---

### Visualizando (Mermaid)

```mermaid
classDiagram
    class Carro {
        +String cor
        +acelerar()
    }
    Ferrari --|> Carro : É um
    Fusca --|> Carro : É um
```

---

## 3. Java e a JVM ♻️

"Write Once, Run Anywhere" (Escreva uma vez, rode em qualquer lugar).

- O Java não compila para Binário direto.
- Ele compila para **Bytecode** (`.class`).
- A **JVM** (Máquina Virtual Java) roda esse Bytecode em qualquer sistema (Windows, Linux, Android, Geladeira).

---

## 4. Os 3 Pilares da OO 🏛️

1.  Encapsulamento
2.  Herança
3.  Polimorfismo

---

### Encapsulamento 🛡️

Proteger os dados. Ninguém mexe no cofre do banco direto.

- **Private**: Só a classe vê.
- **Public**: Todo mundo vê.
- **Getters/Setters**: Porteiros que controlam o acesso.

```java
private double saldo;

public void depositar(double valor) {
    if (valor > 0) saldo += valor;
}
```

---

### Herança 🧬

Reaproveitar código.

- `Cachorro` **é um** `Animal`.
- `Gato` **é um** `Animal`.
- Tudo que `Animal` tem, eles herdam (nome, idade).

```java
public class Cachorro extends Animal { ... }
```

---

### Polimorfismo 🎭

Muitas formas.

- O método `fazerSom()` existe em Animal.
- No Cachorro, ele faz "Au Au".
- No Gato, ele faz "Miau".
- O mesmo método se comporta diferente.

---

## 5. Spring Boot 🍃

Java não é só "tela preta".
É a linguagem nº 1 em Bancos e Grandes Empresas.

- **Spring Boot**: Framework para criar APIs Web.
- Tira toda a configuração chata.

---

### Exemplo de API

```java
@RestController
public class OlaController {
    
    @GetMapping("/ola")
    public String dizerOla() {
        return "Olá, Mundo Java Web!";
    }
}
```

---

## Exercício Mental 🧠

Modele um sistema de **Venda**.

- Classes: `Produto`, `Cliente`, `Venda`.
- Atributos: `Preco`, `Nome`.
- Métodos: `CalcularTotal()`, `Pagar()`.

---

## Resumo ✅

- **Classe** é molde, **Objeto** é real.
- **JVM** garante portabilidade.
- **Encapsulamento** protege.
- **Herança** reutiliza.
- **Polimorfismo** flexibiliza.

---

## Próxima Aula 🚀

- O concorrente direto do Java.
- Criado pela Microsoft.
- **C# e plataforma .NET**.
- Foco em produtividade.

👉 **Tarefa**: Instalar o JDK (Java Development Kit) e o VS Code Extension Pack for Java!