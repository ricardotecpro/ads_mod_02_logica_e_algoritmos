# Aula 10 - Web Moderna: JS e TS 🌐

---

## Agenda 📅

1.  O Navegador como SO
2.  O DOM (Document Object Model)
3.  JavaScript (Dinamismo)
4.  Node.js (Backend)
5.  TypeScript (Segurança)

---

## 1. O Navegador é o Sistema Operacional 🖥️

- Antigamente: Navegador só mostrava texto.
- Hoje: Roda aplicativos completos (Google Docs, Figma, Spotify).
- **Engine**: V8 (Chrome), SpiderMonkey (Firefox).

---

## 2. O DOM 🌳

**Document Object Model**

- É a árvore de elementos da página.
- O HTML é estático. O DOM é vivo.
- O JavaScript muda o DOM em tempo real.

---

### Visualizando o DOM

```mermaid
graph TD;
    Doc[Document] --> HTML;
    HTML --> Head;
    HTML --> Body;
    Head --> Meta;
    Body --> H1[Título];
    Body --> P[Parágrafo];
    Body --> Button[Botão];
    
    style Doc fill:#f9f;
    style Button fill:#bbf;
```

---

## 3. JavaScript: A Linguagem da Web ⚡

- Única linguagem que roda nativamente no navegador.
- **Interpretada**: Não precisa compilar (o navegador lê e executa).
- **Fracamente Tipada**: `var x = 10` depois `x = "oi"` (Pode, mas cuidado!).

---

### Interatividade (Eventos) 🖱️

O JS reage a **Eventos** (Clique, Teclado, Mouse).

```javascript
const botao = document.querySelector('#meuBotao');

botao.addEventListener('click', () => {
    alert("Você clicou!");
    botao.style.backgroundColor = "red";
});
```

---

## 4. Node.js: JS fora da Caixa 📦

- Antes (2009): JS só rodava no Chrome.
- Ryan Dahl pegou a engine V8 e colocou no servidor.
- Nasceu o **Node.js**.

---

### Por que Node? 🚀

- Mesmo código no Frontend e Backend.
- Extremamente rápido (IO Não-Bloqueante).
- Comunidade gigante (NPM).

---

### Exemplo de Servidor (Express)

```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Olá Mundo do Backend!');
});

app.listen(3000);
```

---

## 5. TypeScript: O JavaScript com Superpoderes 🛡️

- Criado pela Microsoft.
- Adiciona **Tipagem Estática** ao JS.
- O navegador **NÃO** entende TS. Ele precisa ser **Transpilado** para JS.

---

### Por que usar TS? 🤔

JS aceita tudo (o que é ruim em projetos grandes).
TS te avisa do erro **antes** de rodar.

---

### Comparativo

**JavaScript (Perigoso)**
```javascript
function soma(a, b) {
    return a + b;
}
soma(5, "10"); // Retorna "510" (Texto) 😱
```

**TypeScript (Seguro)**
```typescript
function soma(a: number, b: number): number {
    return a + b;
}
soma(5, "10"); // ERRO: "String não é Number" 🚫
```

---

## Frameworks Modernos ⚛️

Ninguém escreve JS puro ("Vanilla") em apps grandes.

- **React** (Meta/Facebook)
- **Angular** (Google)
- **Vue.js** (Comunidade)
- Todos usam Componentes e Estado.

---

## Exercício Rápido ⚡

1.  Abra o Console do Navegador (F12).
2.  Digite `alert("Olá")`.
3.  Digite `document.body.style.backgroundColor = "black"`.
4.  O que aconteceu?

---

## Resumo ✅

- **DOM**: A estrutura da página.
- **JavaScript**: Dá vida ao DOM.
- **Node.js**: JS no servidor.
- **TypeScript**: JS com segurança de tipos.

---

## Próxima Aula 🚀

- O mundo corporativo exige robustez.
- **Java**: A linguagem que roda em 3 bilhões de dispositivos.
- Orientação a Objetos "Raiz".

👉 **Tarefa**: Instalar o Node.js e rodar um `console.log` no terminal!