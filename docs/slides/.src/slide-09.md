# Aula 09 - C e C++: Baixo Nível 🧱

---

## Agenda 📅

1.  História e Importância { .fragment }
2.  Anatomia de um Programa C { .fragment }
3.  Compilação { .fragment }
4.  Gerenciamento de Memória (Stack vs Heap) { .fragment }
5.  Ponteiros { .fragment }
6.  Introdução ao C++ (OOP) { .fragment }

---

## 1. O Pai das Linguagens 👴

- **C (1972)**: Dennis Ritchie (Bell Labs). { .fragment }
- **Base de Tudo**: Windows, Linux, Mac, Android, iOS. { .fragment }
- **Filosofia**: "Confie no programador" (mesmo se ele fizer besteira). { .fragment }

---

### Por que aprender C hoje? 🧐

- Entender como a máquina funciona de verdade. { .fragment }
- Gerenciar memória manualmente. { .fragment }
- Performance extrema (Jogos, Sistemas Embarcados). { .fragment }

---

## 2. Anatomia Básica 🦴

```c
#include <stdio.h>

int main() {
    printf("Olá, Mundo C!");
    return 0;
}
```

---

### Desmontando o Código 🔧

1.  `#include <stdio.h>`: Importa biblioteca de IO (Entrada/Saída). { .fragment }
2.  `int main()`: A função principal. Todo programa começa aqui. { .fragment }
3.  `printf(...)`: Imprime formatado. { .fragment }
4.  `return 0;`: Retorna "Sucesso" para o Sistema Operacional. { .fragment }

---

### O Ponto e Vírgula `;`

- Em C/C++, ele é **OBRIGATÓRIO**. { .fragment }
- O compilador não adivinha onde a linha termina. { .fragment }
- Esquecer `;` é o erro nº 1 de iniciantes. { .fragment }

---

## 3. O Processo de Compilação ⚙️

C é uma linguagem **Compilada**.

1.  **Código Fonte** (`.c`): Texto legível. { .fragment }
2.  **Compilador** (`gcc`): Traduz para Assembly/Machine Code. { .fragment }
3.  **Linker**: Junta com bibliotecas. { .fragment }
4.  **Executável** (`.exe`): Programa final. { .fragment }

---

## 4. Memória: Stack vs Heap 🧠

Onde seus dados moram?

---

### Visualizando a Memória

```mermaid
graph TD;
    subgraph RAM
    Stack["Stack (Pilha)"] --- V["Locais\nAutomáticas\nRápidas"];
    Heap["Heap (Monte)"] --- D["Dinâmicas\nManuais\nLentas"];
    end
    style Stack fill:#f9f;
    style Heap fill:#bbf;
```

---

### Stack (Pilha) 🥞

- Variáveis normais: `int idade = 20;` { .fragment }
- Criada e destruída automaticamente. { .fragment }
- Tamanho fixo e pequeno. { .fragment }

---

### Heap (Monte) 🏔️

- Memória dinâmica: `malloc()` ou `new`. { .fragment }
- Você pede memória ao sistema. { .fragment }
- **Cuidado**: Você precisa devolver (`free` ou `delete`), senão vaza memória (Memory Leak)! { .fragment }

---

## 5. Ponteiros: O Superpoder ⚡

Um ponteiro não guarda o valor. Guarda o **ENDEREÇO**.

- `int x = 10;` (Valor 10) { .fragment }
- `int *p = &x;` (Endereço onde o 10 mora, ex: `0x7ffee4`) { .fragment }

---

### Para que serve? 🤷

1.  Modificar variáveis originais dentro de funções. { .fragment }
2.  Alocar memória dinâmica. { .fragment }
3.  Criar estruturas complexas (Listas, Árvores). { .fragment }

> "Com grandes poderes vêm grandes responsabilidades." (E Segmentation Faults).

---

## 6. Introdução ao C++ 🚀

C++ = C + Classes (OOP).

- Mantém a performance do C. { .fragment }
- Adiciona organização de objetos. { .fragment }
- Base para Jogos (Unreal) e Softwares Pesados (Chrome, Photoshop). { .fragment }

---

### Exemplo C++ 🚗

```cpp
#include <iostream>
using namespace std;

class Carro {
public:
    void buzinar() {
        cout << "Bi Bi!" << endl;
    }
};

int main() {
    Carro meuCarro;
    meuCarro.buzinar();
    return 0;
}
```

---

### Diferenças C vs C++

| Feature | C | C++ |
| :--- | :--- | :--- |
| **Paradigma** | Estruturado | Orientado a Objetos (Multi) |
| **Output** | `printf()` | `cout <<` |
| **Input** | `scanf()` | `cin >>` |
| **Extensão** | `.c` | `.cpp` |

---

## Termynal: Compilando 🖥️

<div data-termynal class="termy">
    <span data-ty="input">gcc programa.c -o programa</span>
    <span data-ty="progress">Compilando...</span>
    <span data-ty="input">./programa</span>
    <span data-ty>Olá Mundo C!</span>
</div>

---

## Resumo ✅

- C é a mãe de todas. { .fragment }
- **Compilador** traduz para binário. { .fragment }
- **Ponteiros** acessam memória direta. { .fragment }
- **C++** adiciona Classes ao poder do C. { .fragment }

---

## Próxima Aula 🚀

- Sair do "Baixo Nível". { .fragment }
- Ir para o mundo corporativo e robusto. { .fragment }
- **Java**: "Escreva uma vez, rode em qualquer lugar". { .fragment }

👉 **Tarefa**: Instalar o Code::Blocks ou configurar GCC no VS Code!