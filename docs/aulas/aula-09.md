# Aula 09 - C e C++: Baixo Nível e Performance 🧱

!!! tip "Objetivo"
    **Objetivo**: Entender o que acontece "por baixo do capô". C e C++ te dão controle total sobre a memória do computador.

---

## 1. Linguagem C: O Pai das Linguagens Modernas 👴

Criada em 1972, quase tudo que você usa hoje (Windows, Linux, Android) tem C no núcleo.
É uma linguagem **Estruturada** e **Compilada**.

### A Estrutura Básica

```c
#include <stdio.h> // Importa biblioteca de IO

int main() {
    printf("Ola, Mundo C!");
    return 0;
}
```

### Visualizando a Memória (Stack vs Heap)
Em C, você gerencia onde os dados ficam.

```mermaid
graph TD;
    subgraph RAM
    Stack["Stack (Pilha)"] --- V["Variáveis Locais\nRápidas"];
    Heap["Heap (Monte)"] --- D["Dados Dinâmicos\nLentos"];
    end
    style Stack fill:#f9f;
    style Heap fill:#bbf;
```

### Simulando Compilação (Termynal)

```termynal
$ gcc ola.c -o ola
> Compilando...

$ ./ola
Ola, Mundo C!
```

---

## 2. Ponteiros: O Superpoder (e o Perigo) ⚡

Um ponteiro não guarda um valor (como `10`), ele guarda o **Endereço da Memória** onde o `10` está.

```c
int numero = 10;
int *ponteiro = &numero; // Guarda o endereço de 'numero'
```

!!! warning
    Ponteiros errados podem travar o sistema (o famoso "Segmentation Fault").

---

## 3. C++: Adicionando Objetos 🚀

C++ mantém a velocidade do C, mas adiciona **Classes** e **Objetos** para organizar códigos gigantes.

### Classes e Objetos

```cpp
#include <iostream>
using namespace std;

class Carro {
public:
    string marca;
    void buziar() {
        cout << "Bi Bi!" << endl;
    }
};

int main() {
    Carro meuCarro;
    meuCarro.marca = "Ferrari";
    meuCarro.buziar();
    return 0;
}
```

---

## 4. Exercícios de Fixação 📝

1.  **Fácil**: Escreva um programa em C que leia a idade e mostre se é maior de idade.
2.  **Médio (C++)**: Crie uma classe `Retangulo` com atributos `largura` e `altura` e um método `calcularArea()`.
3.  **Desafio (Ponteiros)**: Crie duas variáveis `a` e `b`. Use uma função `trocar(&a, &b)` que receba ponteiros e troque os valores das variáveis originais.

---
**Próxima Aula**: Vamos sair da "tela preta" e ir para a Web! [JavaScript e TypeScript](./aula-10.md).