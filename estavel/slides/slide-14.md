# Aula 14 - Sistemas Modernos: Rust e Go 🦀🐹

---

## Agenda 📅

1.  O Problema do C/C++ { .fragment }
2.  Rust: Segurança de Memória { .fragment }
3.  Go: Concorrência Simples { .fragment }
4.  Comparativo { .fragment }
5.  Quando usar? { .fragment }

---

## 1. O Problema do C/C++ 💥

- C/C++ são rápidos, mas perigosos. { .fragment }
- **70% das vulnerabilidades** de segurança são erros de memória (Microsoft). { .fragment }
- Buffer Overflow, Use-After-Free. { .fragment }

---

## 2. Rust 🦀

- Criada pela Mozilla. { .fragment }
- Promessa: **Performance de C++ com Segurança de Memória**. { .fragment }
- Sem Garbage Collector (GC). { .fragment }
- Sem Tela Azul. { .fragment }

---

### O Segredo: Ownership (Posse) 🔑

- Cada dado tem **um único dono**. { .fragment }
- Quando o dono muda, o antigo perde o acesso. { .fragment }
- O compilador verifica isso **antes** de rodar. { .fragment }

---

### Visualizando Ownership

```mermaid
graph LR;
    A["Variável A\n(Dona do Dado)"] -- "Move" --> B["Variável B\n(Nova Dona)"];
    style A fill:#f9f;
    style B fill:#bbf;
    
    NoteA["A morre.\nNão pode mais acessar!"] --- A
```

---

### Código Rust

```rust
fn main() {
    let a = String::from("Olá");
    let b = a; // MOVEU para b
    
    // println!("{}", a); // ERRO DE COMPILAÇÃO!
    // O compilador te salva de usar memória inválida.
}
```

---

## 3. Go (Golang) 🐹

- Criada pelo Google (Rob Pike, Ken Thompson). { .fragment }
- Foco: **Simplicidade** e **Google Scale**. { .fragment }
- Compila ultra-rápido. { .fragment }

---

### Concorrência Fácil (Goroutines) 🧵

- Threads são pesadas. { .fragment }
- Goroutines são leves (milhares em poucos MBs). { .fragment }
- **Channels**: Forma segura de conversar entre processos. { .fragment }

---

### Visualizando Channels

```mermaid
graph LR;
    T1[Goroutine A] -->|Envia 'Ping'| Canal((Channel));
    Canal -->|Recebe 'Ping'| T2[Goroutine B];
    
    style Canal fill:#ff9;
```

---

### Código Go

```go
package main
import "fmt"

func main() {
    mensagens := make(chan string)

    go func() { mensagens <- "Ping" }()

    msg := <-mensagens
    fmt.Println(msg)
}
```

---

## 4. Comparativo ⚖️

| Feature | Rust 🦀 | Go 🐹 |
| :--- | :--- | :--- |
| **Foco** | Controle, Segurança Absoluta | Simplicidade, Web Services |
| **Aprendizado** | Curva Íngreme (Dificil) | Muito Fácil |
| **Performance** | Extrema (Zero-Cost) | Muito Boa (Com GC) |
| **Uso** | Drivers, Engines, Crypto | Microservices, Cloud, APIs |

---

## Termynal: Execução 🖥️

<div data-termynal class="termy">
    <span data-ty="input">cargo run</span>
    <span data-ty="progress">Compiling...</span>
    <span data-ty>Hello Rust! (Safe)</span>
    <span data-ty="input">go run main.go</span>
    <span data-ty>Hello Go! (Fast Build)</span>
</div>

---

## Resumo ✅

- **Rust**: Substitui C++ onde segurança é crítica. { .fragment }
- **Go**: Substitui Java/Node onde concorrência é crítica. { .fragment }
- Ambas são o futuro da Infraestrutura (Docker, Kubernetes). { .fragment }

---

## Próxima Aula 🚀

- Sair do Servidor. { .fragment }
- Ir para o dispositivo que está na sua mão. { .fragment }
- **Desenvolvimento Mobile**: Flutter (Dart) e Nativo. { .fragment }

👉 **Tarefa**: Instalar o Go e rodar um "Olá Mundo"!