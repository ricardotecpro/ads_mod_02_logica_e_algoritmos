# Aula 04 - Estrutura Condicional 🔀

---

## Agenda 📅

1.  O Desvio Lógico ("Se...") { .fragment }
2.  Operadores Relacionais { .fragment }
3.  Estrutura Se-Entao-Senao { .fragment }
4.  Operadores Lógicos (E, OU, NÃO) { .fragment }
5.  Estrutura Escolha-Caso { .fragment }

---

## 1. O Desvio Lógico 🤔

Até agora, nossos programas eram uma linha reta.
Mas a vida é feita de escolhas.

- **Se** chover, pego guarda-chuva. { .fragment }
- **Senão**, vou de bicicleta. { .fragment }

---

### Visualizando a Decisão

```mermaid
graph TD;
    Inicio([Início]) --> Pergunta{Está Sol?};
    Pergunta -- Sim --> A[Praia];
    Pergunta -- Não --> B[Netflix];
    A --> Fim([Fim]);
    B --> Fim;
```

---

## 2. Operadores Relacionais 📏

Para o computador decidir, ele precisa **comparar**.
A resposta é sempre **Verdadeiro** ou **Falso**.

---

### Os Comparadores

| Símbolo | Significado | Exemplo | Resultado |
| :---: | :--- | :--- | :--- |
| `>` | Maior que | `10 > 5` | V |
| `<` | Menor que | `3 < 8` | V |
| `==` | Igual a | `5 == 5` | V |
| `!=` | Diferente | `5 != 3` | V |
| `>=` | Maior/Igual | `10 >= 10` | V |

---

## 3. Sintaxe Básica (Se-Entao) 📝

```visualg
se (nota >= 7) entao
   escreva("Aprovado!")
fimse
```

- Se a condição for **Verdadeira**, ele executa o bloco. { .fragment }
- Se for **Falsa**, ele pula. { .fragment }

---

### O "Senao" (O Plano B)

E se for Falso? Usamos o `senao`.

```visualg
se (nota >= 7) entao
   escreva("Aprovado!")
senao
   escreva("Reprovado!")
fimse
```

---

## 4. Operadores Lógicos 🔗

Às vezes, uma condição só não basta.

- Quero ir à praia **SE** tiver sol **E** for sábado. { .fragment }

---

### Operador E (AND) 🤝

- Exige que **TODAS** as condições sejam verdadeiras. { .fragment }

| A | B | A e B |
| :---: | :---: | :---: |
| V | V | **V** |
| V | F | F |
| F | V | F |
| F | F | F |

---

### Operador OU (OR) 🤷

- Exige que **PELO MENOS UM** seja verdadeiro. { .fragment }

| A | B | A ou B |
| :---: | :---: | :---: |
| V | V | **V** |
| V | F | **V** |
| F | V | **V** |
| F | F | F |

---

### Operador NÃO (NOT) 🚫

- Inverte o resultado. { .fragment }

| A | NÃO A |
| :---: | :---: |
| V | F |
| F | V |

---

## Exemplo Prático: Média Escolar 🎓

Vamos melhorar nosso cálculo de média.

- Media >= 7: Aprovado. { .fragment }
- Media >= 5 E Media < 7: Recuperação. { .fragment }
- Media < 5: Reprovado. { .fragment }

---

### O Código (Aninhado)

```visualg
se (media >= 7) entao
   escreval("Aprovado")
senao
   se (media >= 5) entao
      escreval("Recuperação")
   senao
      escreval("Reprovado")
   fimse
fimse
```

---

## 5. Estrutura Escolha-Caso 🚦

Quando temos muitas opções fixas (como um Menu).
Evita aquele monte de `se-senao-se-senao`.

---

### Exemplo: Menu

```visualg
escolha (opcao)
   caso 1
      escreva("Iniciar Jogo")
   caso 2
      escreva("Configurações")
   caso 3
      escreva("Sair")
   outrocaso
      escreva("Opção Inválida")
fimescolha
```

---

### Quando usar qual? 🤔

- **SE**: Para testar intervalos (`idade > 18`), condições complexas (`E`, `OU`). { .fragment }
- **ESCOLHA**: Para valores exatos (Menus, Códigos de produto). { .fragment }

---

## Exercício Rápido ⚡

**Par ou Ímpar?**

1.  Leia um número. { .fragment }
2.  Verifique se o resto da divisão por 2 é zero. { .fragment }
3.  Se for, é Par. { .fragment }
4.  Senão, é Ímpar. { .fragment }

---

## Resumo ✅

- **Se/Então/Senão**: Tomada de decisão. { .fragment }
- **Relacionais**: `>`, `<`, `=`, `!=`. { .fragment }
- **Lógicos**: `E`, `OU`, `NÃO`. { .fragment }
- **Escolha**: Ótimo para menus. { .fragment }

---

## Próxima Aula 🚀

- E se eu quiser repetir um comando 1000 vezes? { .fragment }
- **Loops** (Laços de Repetição). { .fragment }
- `Enquanto`, `Para`, `Repita`. { .fragment }

👉 **Tarefa**: Fazer o exercício do Bhaskara!