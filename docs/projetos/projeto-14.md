# Projeto 14 - Sistema de Mensageria 🦀🐹

!!! tip "Objetivo"
    **Objetivo**: Explorar conceitos de programação concorrente e paralela, utilizando Canais (Go) ou Threads com Mutex (Rust).

---

## O Desafio 🎯
Implemente um sistema onde múltiplos produtores (Clientes) enviam dados para um único processador central (Servidor).

## Opção A: Go (Goroutines e Channels)
1.  Crie uma função `Servidor` que fica em um loop infinito esperando mensagens de um canal.
2.  Lance 3 `Goroutines` de Clientes.
3.  Cada cliente deve enviar 5 mensagens numeradas (Ex: "Msg 1 do Cliente A").
4.  O servidor deve imprimir as mensagens conforme elas chegam.

## Opção B: Rust (Safety e Concorrência)
1.  Crie um programa que faça uma soma pesada (ex: de 1 a 1.000.000).
2.  Divida o intervalo em 4 partes.
3.  Dispare uma `Thread` para cada parte.
4.  Use `Arc` e `Mutex` (ou MPSC Channels) para consolidar o resultado final com segurança de memória.

## O que você vai aprender? 🧠
Você verá que a ordem de execução das mensagens/contagens é imprevisível, entendendo como o sistema operacional lida com multitarefa.