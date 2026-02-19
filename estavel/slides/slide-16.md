# Aula 16 - PHP e o Lado do Servidor 🐘

---

## Agenda 📅

1.  Como a Web Funciona?
2.  PHP: O Motor da Internet
3.  Arquitetura MVC
4.  Laravel (Framework)
5.  Projeto Final

---

## 1. O Ciclo da Web 🌍

Client vs Server.

- **Cliente (Browser)**: Pede coisas (Request).
- **Servidor**: Processa e Devolve (Response).
- **Banco de Dados**: Guarda as informações.

---

### Requisição e Resposta (Sequence)

```mermaid
sequenceDiagram
    participant Browser
    participant Servidor
    participant Banco
    
    Browser->>Servidor: 1. GET /perfil
    Servidor->>Banco: 2. SELECT * FROM users
    Banco-->>Servidor: 3. Dados (João, 25)
    Servidor-->>Browser: 4. HTML Pronto
```

---

## 2. O Que é PHP? 🐘

**P**HP: **H**ypertext **P**reprocessor.

- Roda no Servidor (Back-end).
- Gera HTML dinâmico.
- Fácil de hospedar (qualquer servidor barato tem).
- Poderoso (Facebook, Wikipedia, WordPress).

---

### Código PHP

```php
<?php
    $nome = "Maria";
    $saldo = 100.50;
    
    echo "<h1>Olá, $nome!</h1>";
    echo "<p>Saldo: $saldo</p>";
?>
```

---

## 3. Arquitetura MVC 🏗️

Para organizar sites grandes, não misturamos código.

- **M**odel (Modelo): Dados e Banco.
- **V**iew (Visão): HTML e Telas.
- **C**ontroller (Controlador): A Lógica.

---

### Fluxo MVC

```mermaid
graph LR;
    User -->|Rota| Controller;
    Controller -->|Pede| Model;
    Model -->|Devolve| Controller;
    Controller -->|Envia| View;
    View -->|HTML| User;
```

---

## 4. Laravel 🚀

O Framework PHP mais popular.

- Sintaxe elegante.
- Ferramentas prontas (Login, Email, Banco).
- "O PHP Moderno".

```php
// Rota simples em Laravel
Route::get('/', function () {
    return view('welcome');
});
```

---

## Projeto Final do Curso 🏆

**Mural de Recados Fullstack**

- **Banco**: MySQL (`recados`: id, mensagem).
- **Back**: PHP (Busca recados).
- **Front**: HTML/CSS (Mostra recados).
- Use tudo que aprendeu: Lógica, Loops, Vetores (Dados do banco), HTML.

---

## Termynal: Servidor PHP 🖥️

<div data-termynal class="termy">
    <span data-ty="input">php -S localhost:8000</span>
    <span data-ty="progress">Listening on localhost:8000...</span>
    <span data-ty>Requisição recebida: /index.php</span>
    <span data-ty>200 OK</span>
</div>

---

## Resumo do Módulo ✅

1.  **Lógica**: Algoritmos, Fluxogramas.
2.  **Dados**: Variáveis, Vetores, Matrizes.
3.  **Tecnologias**:
    - Baixo nível (C/C++).
    - Web (JS, PHP).
    - Mobile (Flutter).
    - Corporativo (Java, C#).

---

## Parabéns! 🎓

Você completou a jornada de Lógica e Algoritmos.
Você agora tem a **base** para aprender qualquer linguagem.

**Próximos Passos?**
- Escolha uma área (Front, Back, Mobile, Dados).
- Aprofunde-se na linguagem escolhida.
- **PRATIQUE!**

👉 **Projeto Final**: Entregar o Mural de Recados!