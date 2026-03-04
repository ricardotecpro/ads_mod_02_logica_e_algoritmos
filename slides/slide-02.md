# Aula 02 - Ambiente e Ferramentas 🛠️

---

## Agenda 📅

1.  O Ciclo de Vida do Código <!-- .element: class="fragment" -->
2.  Ferramentas de Aprendizado (Low Code) <!-- .element: class="fragment" -->
3.  Visual Studio Code (A Ferramenta Real) <!-- .element: class="fragment" -->
4.  O Terminal (Sem Medo!) <!-- .element: class="fragment" -->
5.  Instalação e Configuração <!-- .element: class="fragment" -->

---

## 1. O Ciclo de Vida do Código 🔄

Como o computador entende o que escrevemos?

- **Nós**: Falamos Inglês/Português (Texto). <!-- .element: class="fragment" -->
- **Computador**: Fala Energia (0 e 1). <!-- .element: class="fragment" -->
- **O Problema**: Tradução. <!-- .element: class="fragment" -->

---

## As 3 Etapas 🚦

1.  **Código Fonte**: O texto que você digita. <!-- .element: class="fragment" -->
2.  **Compilação/Interpretação**: A tradução mágica. <!-- .element: class="fragment" -->
3.  **Execução (Binário)**: O programa rodando. <!-- .element: class="fragment" -->

---

### Visualizando o Processo

```mermaid
graph LR;
    A["Código Fonte\n(Humano)"] -->|Compilador| B["Binário\n(Máquina)"];
    B -->|CPU| C["Execução\n(Ação)"];
    style A fill:#f9f;
    style B fill:#bbf;
    style C fill:#bfb;
```

---

## Código Fonte 📝

- Arquivos de texto simples (`.alg`, `.py`, `.c`, `.java`). <!-- .element: class="fragment" -->
- Legível para humanos. <!-- .element: class="fragment" -->
- Exemplo: <!-- .element: class="fragment" -->
    ```visualg
    escreva("Olá Mundo")
    ```

---

## Compilador ⚙️

- O "Tradutor". <!-- .element: class="fragment" -->
- Verifica se você escreveu certo (Sintaxe). <!-- .element: class="fragment" -->
- Transforma em linguagem de máquina. <!-- .element: class="fragment" -->
- Se tiver erro, ele GRITA (Erro de Compilação). <!-- .element: class="fragment" -->

---

## Binário / Executável 🚀

- O resultado final. <!-- .element: class="fragment" -->
- `.exe` (Windows), App Mobile. <!-- .element: class="fragment" -->
- O usuário final só vê isso. <!-- .element: class="fragment" -->
- Não dá para ler (só números e símbolos estranhos). <!-- .element: class="fragment" -->

---

## 2. Ferramentas Low Code 🧩

Para começar **sem frustração**.

- Foco na **Lógica**. <!-- .element: class="fragment" -->
- Esqueça "ponto-e-vírgula" por enquanto. <!-- .element: class="fragment" -->
- VisualG e Scratch. <!-- .element: class="fragment" -->

---

### VisualG 🟦

- **Linguagem**: Portugol (Português Estruturado). <!-- .element: class="fragment" -->
- **Interface**: Simples, leve. <!-- .element: class="fragment" -->
- **Diferencial**: Mostra o valor das variáveis em tempo real (Memória). <!-- .element: class="fragment" -->
- **Uso**: Exclusivo para ensino no Brasil. <!-- .element: class="fragment" -->

---

### Exemplo VisualG

```visualg
Algoritmo "Exemplo"
Var
   nome : caractere
Inicio
   escreva("Qual seu nome? ")
   leia(nome)
   escreva("Olá, ", nome)
Fimalgoritmo
```
> Parece português, funciona como código.

---

### Scratch 🐱

- Criado pelo MIT. <!-- .element: class="fragment" -->
- Programação em **Blocos** (Lego). <!-- .element: class="fragment" -->
- Impossível errar sintaxe (os blocos só encaixam se estiver certo). <!-- .element: class="fragment" -->
- Ótimo para entender loops e eventos. <!-- .element: class="fragment" -->

---

## 3. Visual Studio Code (VS Code) 💻

A ferramenta profissional.

- Gratuito (Microsoft). <!-- .element: class="fragment" -->
- Leve. <!-- .element: class="fragment" -->
- **Extensível**. <!-- .element: class="fragment" -->

---

### Por que VS Code? 🌟

1.  **IntelliSense**: Autocomplete inteligente. <!-- .element: class="fragment" -->
2.  **Multi-Linguagem**: Python, Java, C++, HTML... tudo num lugar só. <!-- .element: class="fragment" -->
3.  **Terminal Integrado**: Não precisa abrir janelas extras. <!-- .element: class="fragment" -->
4.  **Comunidade**: Milhares de plugins. <!-- .element: class="fragment" -->

---

### Extensões Essenciais 🧩

Sem elas, ele é apenas um bloco de notas.

- **Portuguese (Brazil)**: Traduz o menu. <!-- .element: class="fragment" -->
- **Material Icon Theme**: Ícones bonitos para arquivos. <!-- .element: class="fragment" -->
- **Code Runner**: Roda código com um clique. <!-- .element: class="fragment" -->
- **Live Server**: Para Web (HTML). <!-- .element: class="fragment" -->

---

## 4. O Terminal (Tela Preta) 🖥️

Não tenha medo da tela preta!

- É o modo "Hacker" (mas simples). <!-- .element: class="fragment" -->
- Controle total do sistema. <!-- .element: class="fragment" -->
- Mais rápido que clicar com o mouse. <!-- .element: class="fragment" -->

---

### Comandos Básicos (Windows/Linux)

| Comando | Função | Exemplo |
| :--- | :--- | :--- |
| `cd` | Change Directory (Mudar Pasta) | `cd projetos` |
| `ls` ou `dir` | List (Listar arquivos) | `ls` |
| `mkdir` | Make Directory (Criar Pasta) | `mkdir aula01` |
| `clear` ou `cls` | Clear Screen (Limpar) | `cls` |

---

## 5. Prática: Olá Mundo 🌍

Vamos criar nosso primeiro programa no VisualG.

1.  Abra o VisualG. <!-- .element: class="fragment" -->
2.  No bloco `Inicio`, digite: <!-- .element: class="fragment" -->
    ```visualg
    Escreval("Olá, Mundo!")
    ```
3.  Aperte **F9** (Executar). <!-- .element: class="fragment" -->

---

### Onde Configurar? 🛠️

Preparamos guias passo a passo para você instalar tudo.

- [Setup 01 - VisualG](../setups/setup-01.md) (Comece aqui!) <!-- .element: class="fragment" -->
- [Setup 03 - VS Code](../setups/setup-03.md) (Para depois) <!-- .element: class="fragment" -->

---

## Resumo ✅

- Código Fonte -> Compilador -> Binário. <!-- .element: class="fragment" -->
- VisualG = Treino de Lógica. <!-- .element: class="fragment" -->
- VS Code = ferramenta Profissional. <!-- .element: class="fragment" -->
- Terminal = Poder e Velocidade. <!-- .element: class="fragment" -->

---

## Próxima Aula 🚀

- Entrar na "Mente do Computador". <!-- .element: class="fragment" -->
- **Variáveis**: Como o computador guarda informações? <!-- .element: class="fragment" -->
- **Tipos de Dados**: Texto, Número Inteiro, Número Real, Lógico. <!-- .element: class="fragment" -->

👉 **Tarefa de Casa**: Instalar VisualG e rodar o "Olá Mundo".