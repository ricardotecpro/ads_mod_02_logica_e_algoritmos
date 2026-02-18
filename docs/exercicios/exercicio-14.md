# Exercícios 14 - Rust e Go 🦀🐹

!!! tip "Objetivo"
    **Objetivo**: Sistemas e Concorrência.

---

## 🟢 Fáceis

1.  **Rust Hello**: Instale o Rust e rode um "Olá Mundo" com `cargo run`.
2.  **Go Hello**: Instale o Go e rode um "Olá Mundo" com `go run main.go`.

## 🟡 Médios

3.  **Ownership (Rust)**:
    *   Crie uma String `s1 = "Teste"`.
    *   Mova para `s2`.
    *   Tente imprimir `s1` e veja o erro de compilação. Explique por que aconteceu.
4.  **Goroutine Simples (Go)**:
    *   Crie uma função que imprime "Processando..." 5 vezes com um delay de 1 segundo.
    *   Chame-a com `go` na frente.
    *   Chame-a normalmente na thread principal.
    *   Veja as mensagens se misturarem.

## 🔴 Desafio

5.  **Calculadora Segura (Rust)**:
    *   Crie uma função de divisão que retorna um `Result<f64, String>`.
    *   Se o divisor for 0, retorne `Err("Divisão por zero")`.
    *   Senão, retorne `Ok(resultado)`.
    *   No `main`, trate o erro com `match`.