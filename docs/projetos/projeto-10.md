# Projeto 10 - To-Do List Interativa 🌐

!!! tip "Objetivo"
    **Objetivo**: Praticar a manipulação do DOM (Document Object Model), tratamento de eventos e persistência local no navegador usando JavaScript ou TypeScript.

---

## O Desafio 🎯
Transforme uma página estática em um aplicativo funcional. Crie uma lista de tarefas onde o usuário possa adicionar, concluir e remover itens em tempo real.

## Requisitos Técnicos
1.  **Interface (HTML/CSS)**:
    *   Um campo de texto (`input`).
    *   Um botão "Adicionar".
    *   Uma lista vazia (`ul`).
2.  **Funcionalidades (JS/TS)**:
    *   **Adição**: Capturar o texto e criar um novo `li` dinamicamente.
    *   **Conclusão**: Adicionar um checkbox que, ao ser marcado, aplica um estilo de "riscado" ao texto da tarefa.
    *   **Remoção**: Adicionar um botão "Excluir" ao lado de cada tarefa.
3.  **Persistência (Bônus)**:
    *   Use `localStorage` para que a lista não desapareça quando a página for atualizada.

## Estrutura do Código (Sugestão)
```javascript
const btnAdd = document.querySelector('#btn-add');
const input = document.querySelector('#tarefa-input');

btnAdd.addEventListener('click', () => {
    // Lógica para criar elemento e dar append na lista
});
```

## Dica Visual 🎨
Use CSS para dar um feedback visual claro quando uma tarefa for concluída (mude a cor de fundo ou a opacidade).