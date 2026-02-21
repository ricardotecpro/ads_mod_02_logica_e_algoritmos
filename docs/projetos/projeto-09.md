# Projeto 09 - Gerenciador de Memória 🧱

!!! tip "Objetivo"
    **Objetivo**: Compreender o gerenciamento manual de memória, o uso de ponteiros e a alocação dinâmica (Heap), pilares fundamentais de linguagens de baixo nível como C e C++.

---

## O Desafio 🎯
Você deve criar um programa capaz de manipular dados diretamente na memória RAM. O desafio é gerenciar um vetor cujo tamanho só é conhecido quando o programa está rodando.

## Requisitos Técnicos (C)
1.  **Entrada**: Pergunte ao usuário quantos números ele deseja armazenar.
2.  **Alocação**: Use `malloc` para reservar exatamente o espaço necessário no Heap.
3.  **Processamento**:
    *   Preencha o vetor com valores.
    *   Implemente uma função que inverta o vetor **in-place** (trocando os elementos de posição sem criar um vetor reserva).
4.  **Liberação**: Use `free` para devolver a memória ao sistema antes de encerrar.

## Desafio Extra (C++) ⭐
Implemente o mesmo sistema usando uma `Class VetorDinamico`. 
- Utilize o construtor para alocar memória (`new`).
- Utilize o **destrutor** para garantir a liberação automática (`delete[]`).

## Exemplo de Saída
```text
Quantos elementos? 3
Digite os valores: 10, 20, 30
--- Invertendo ---
Resultado: 30, 20, 10
Memória liberada com sucesso.
```