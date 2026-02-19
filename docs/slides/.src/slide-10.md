# Aula 10 - Web Moderna: JS e TS 🌐

---

## Agenda 📅

1.  O Navegador como SO { .fragment }
2.  O DOM (Document Object Model) { .fragment }
3.  JavaScript (Dinamismo) { .fragment }
4.  Node.js (Backend) { .fragment }
5.  TypeScript (Segurança) { .fragment }

---

## 1. O Navegador é o Sistema Operacional 🖥️

- Antigamente: Navegador só mostrava texto. { .fragment }
- Hoje: Roda aplicativos completos (Google Docs, Figma, Spotify). { .fragment }
- **Engine**: V8 (Chrome), SpiderMonkey (Firefox). { .fragment }

---

## 2. O DOM 🌳

**Document Object Model**

- É a árvore de elementos da página. { .fragment }
- O HTML é estático. O DOM é vivo. { .fragment }
- O JavaScript muda o DOM em tempo real. { .fragment }

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

- Única linguagem que roda nativamente no navegador. { .fragment }
- **Interpretada**: Não precisa compilar (o navegador lê e executa). { .fragment }
- **Fracamente Tipada**: `var x = 10` depois `x = "oi"` (Pode, mas cuidado!). { .fragment }

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

- Antes (2009): JS só rodava no Chrome. { .fragment }
- Ryan Dahl pegou a engine V8 e colocou no servidor. { .fragment }
- Nasceu o **Node.js**. { .fragment }

---

### Por que Node? 🚀

- Mesmo código no Frontend e Backend. { .fragment }
- Extremamente rápido (IO Não-Bloqueante). { .fragment }
- Comunidade gigante (NPM). { .fragment }

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

- Criado pela Microsoft. { .fragment }
- Adiciona **Tipagem Estática** ao JS. { .fragment }
- O navegador **NÃO** entende TS. Ele precisa ser **Transpilado** para JS. { .fragment }

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

- **React** (Meta/Facebook) { .fragment }
- **Angular** (Google) { .fragment }
- **Vue.js** (Comunidade) { .fragment }
- Todos usam Componentes e Estado. { .fragment }

---

## Exercício Rápido ⚡

1.  Abra o Console do Navegador (F12). { .fragment }
2.  Digite `alert("Olá")`. { .fragment }
3.  Digite `document.body.style.backgroundColor = "black"`. { .fragment }
4.  O que aconteceu? { .fragment }

---

## Resumo ✅

- **DOM**: A estrutura da página. { .fragment }
- **JavaScript**: Dá vida ao DOM. { .fragment }
- **Node.js**: JS no servidor. { .fragment }
- **TypeScript**: JS com segurança de tipos. { .fragment }

---

## Próxima Aula 🚀

- O mundo corporativo exige robustez. { .fragment }
- **Java**: A linguagem que roda em 3 bilhões de dispositivos. { .fragment }
- Orientação a Objetos "Raiz". { .fragment }

👉 **Tarefa**: Instalar o Node.js e rodar um `console.log` no terminal!