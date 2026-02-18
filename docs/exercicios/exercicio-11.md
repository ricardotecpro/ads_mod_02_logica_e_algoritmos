# Exercícios 11 - Java e POO ☕

> [!TIP]
> **Objetivo**: Criar sistemas robustos com Classes.

---

## 🟢 Fáceis

1.  **Classe Pessoa**: Crie uma classe `Pessoa` com atributos `nome` e `idade`. No `main`, crie um objeto e imprima seus dados.
2.  **Calculadora Estática**: Crie uma classe `Calculadora` com um método `static somar(int a, int b)`. Chame-o direto do `main` sem criar objeto (`Calculadora.somar(2, 3)`).

## 🟡 Médios

3.  **Encapsulamento**:
    *   Crie uma classe `ContaBancaria`.
    *   Atributo `private double saldo`.
    *   Métodos `public void depositar(double valor)` e `public double getSaldo()`.
    *   Garanta que não dê para depositar valor negativo!
4.  **Herança**:
    *   Classe `Veiculo` (marca, modelo).
    *   Classe `Carro` (herda Veiculo, tem portas).
    *   Classe `Moto` (herda Veiculo, tem cilindradas).
    *   Crie objetos de Carro e Moto e preencha os dados.

## 🔴 Desafio

5.  **Sistema de Folha de Pagamento (Polimorfismo)**:
    *   Classe `Funcionario` com método `calcularSalario()`.
    *   Classe `Gerente` (Ganha bônus de 20%).
    *   Classe `Estagiario` (Ganha metade).
    *   Crie uma lista de funcionários mistos e calcule o total da folha.
