# Aula 01 - Lógica de Programação 🧠

---

## Agenda 📅

1.  O que é Lógica? { .fragment }
2.  O Algoritmo { .fragment }
3.  Pensamento Computacional { .fragment }
4.  Fluxogramas { .fragment }
5.  Ferramentas (VisualG) { .fragment }

---

## 1. O que é Lógica? 🧠

> "A arte de pensar corretamente."

- Organização de ideias. { .fragment }
- Maneira rigorosa de raciocinar. { .fragment }
- **Não** é apenas para computadores! { .fragment }
- Usamos no dia a dia sem perceber. { .fragment }

---

## Lógica no Dia a Dia ☀️

- Se **chover**, levo guarda-chuva. { .fragment }
- Se **estiver sol**, vou à praia. { .fragment }
- Se o **pneu furar**, troco o pneu. { .fragment }
- **Causa** -> **Efeito**. { .fragment }

---

## O Computador é BURRO 🤖

- Ele não "pensa". { .fragment }
- Ele apenas obedece. { .fragment }
- Se você explicar errado, ele fará errado. { .fragment }
- **Programar** = Ensinar o computador. { .fragment }

---

## 2. O Algoritmo 💡

- **Definição**: Sequência de passos finitos e precisos para resolver um problema. { .fragment }
- **Palavras-chave**: { .fragment }
    - **Sequência**: A ordem importa. { .fragment }
    - **Finitos**: Tem que acabar. { .fragment }
    - **Precisos**: Sem "talvez". { .fragment }

---

## Receita de Bolo 🍰

1.  Quebrar ovos. { .fragment }
2.  Misturar farinha. { .fragment }
3.  Assar por 40min. { .fragment }
4.  Comer. { .fragment }

*Se você "Comer" antes de "Assar", vai dar dor de barriga! (Ordem importa)*

---

## Estrutura Básica 🏗️

Todo algoritmo tem 3 fases:

1.  **Entrada** (Ingredientes). { .fragment }
2.  **Processamento** (Misturar/Assar). { .fragment }
3.  **Saída** (Bolo pronto). { .fragment }

---

## 3. Pensamento Computacional 🧩

Os 4 Superpoderes para resolver problemas complexos.

1.  **Decomposição** { .fragment }
2.  **Reconhecimento de Padrões** { .fragment }
3.  **Abstração** { .fragment }
4.  **Algoritmo** { .fragment }

---

### 3.1 Decomposição 🧱

- Quebrar um problema grande em menores. { .fragment }
- Exemplo: **Construir uma Casa**. { .fragment }
    - Fazer fundação. { .fragment }
    - Levantar paredes. { .fragment }
    - Colocar telhado. { .fragment }

---

### 3.2 Reconhecimento de Padrões 🔍

- Identificar o que já vimos antes. { .fragment }
- Exemplo: { .fragment }
    - Dirigir Carro 🚗 { .fragment }
    - Dirigir Caminhão 🚛 { .fragment }
    - Padrão: Volante, Pedais, Câmbio. { .fragment }

---

### 3.3 Abstração 🌫️

- Focar no essencial. { .fragment }
- Ignorar detalhes irrelevantes. { .fragment }
- Exemplo: "Trocar o pneu". { .fragment }
    - Importa: Chave de roda, Macaco. { .fragment }
    - Não importa: Marca da borracha, cor do aro. { .fragment }

---

### 3.4 Algoritmo (Design) 📝

- Escrever o passo a passo final. { .fragment }
- Juntar tudo o que foi planejado. { .fragment }
- O plano de execução. { .fragment }

---

## 4. Fluxogramas 🗺️

A linguagem universal dos programadores.

- Desenho > Texto. { .fragment }
- Padronizado mundialmente. { .fragment }

---

### Símbolos Principais

| Forma | Nome | Função |
| :---: | :--- | :--- |
| `([ ... ])` | **Terminador** | Início/Fim |
| `[ ... ]` | **Processo** | Ação/Cálculo |
| `/ ... /` | **Dados** | Entrada/Saída |
| `{ ... }` | **Decisão** | Pergunta (Sim/Não) |

---

### Exemplo: Lâmpada 💡

```mermaid
graph TD;
    A([Início]) --> B{Lâmpada acende?};
    B -- Não --> C{Plugada?};
    C -- Não --> D[Plugar];
    C -- Sim --> E[Trocar Bulbo];
    B -- Sim --> F([Fim]);
    D --> F;
    E --> F;
```

---

## 5. VisualG e Portugol 💻

- **Portugol**: "Português Estruturado". { .fragment }
- Uma linguagem feita para **aprender**. { .fragment }
- Comandos em português. { .fragment }
- Foco na lógica, não na sintaxe complexa (ainda). { .fragment }

---

### Ferramenta: VisualG

- Gratuito. { .fragment }
- Leve. { .fragment }
- Roda direto no Windows. { .fragment }
- Mostra a memória do computador. { .fragment }

---

### Primeiro Código (Preview)

```visualg
Algoritmo "OlaMundo"
Inicio
   Escreval("Olá, Mundo!")
   Escreval("Eu sou um programador!")
FimAlgoritmo
```

> Veremos isso na prática na próxima aula!

---

## Vamos Praticar? 📝

**Desafio do Lobo/Ovelha/Alface**

- Um barqueiro. { .fragment }
- Lobo come Ovelha. { .fragment }
- Ovelha come Alface. { .fragment }
- Barco só leva 1 passageiro extra. { .fragment }
- Como atravessar todos? { .fragment }

---

## Solução (Algoritmo)

1.  Leva Ovelha. Voltou Vazio. { .fragment }
2.  Leva Lobo. Traz Ovelha. { .fragment }
3.  Deixa Ovelha. Leva Alface. Voltou Vazio. { .fragment }
4.  Leva Ovelha. { .fragment }
5.  FIM. { .fragment }

---

## Resumo ✅

- Lógica = Pensar certo. { .fragment }
- Algoritmo = Sequência de passos. { .fragment }
- 3 Fases: Entrada, Processamento, Saída. { .fragment }
- Fluxogramas ajudam a desenhar a solução. { .fragment }

---

## Próxima Aula 🚀

- Configurar o VisualG. { .fragment }
- Entender **Variáveis** (As caixas da memória). { .fragment }
- Tipos de Dados (Texto, Número, Lógico). { .fragment }

👉 **Instalem o VisualG!**