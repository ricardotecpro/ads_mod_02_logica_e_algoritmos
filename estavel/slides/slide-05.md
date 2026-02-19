# Aula 05 - Estruturas Repetitivas 🔁

---

## Agenda 📅

1.  O Poder da Repetição (Loops) { .fragment }
2.  Estrutura Enquanto (While) { .fragment }
3.  Estrutura Repita (Do-While) { .fragment }
4.  Estrutura Para (For) { .fragment }
5.  Controle de Fluxo (Interrompa) { .fragment }
6.  Teste de Mesa { .fragment }

---

## 1. O Poder da Repetição 🔄

Imagine escrever "Eu não vou jogar bolinha de papel" 100 vezes no quadro.

- **Humano**: Cansa, erra, demora. { .fragment }
- **Computador**: Faz em 1 milissegundo. { .fragment }

---

### O Loop (Laço) ♾️

- Executa um bloco de código **enquanto** uma condição for verdadeira. { .fragment }
- Automatiza tarefas repetitivas. { .fragment }
- Economiza linhas de código. { .fragment }

---

### Visualizando um Loop

```mermaid
graph TD;
    Inicio([Início]) --> Cond{Contador < 5?};
    Cond -- Sim --> Acao["Escrever 'Olá'"];
    Acao --> Inc[Contador + 1];
    Inc --> Cond;
    Cond -- Não --> Fim([Fim]);
```

---

## 2. Enquanto (While) ⏳

- O mais comum. { .fragment }
- Testa a condição **ANTES** de entrar. { .fragment }
- Se a condição for falsa de cara, ele nunca executa. { .fragment }

---

### Sintaxe

```visualg
enquanto (condicao) faca
   // Comandos
fimenquanto
```

---

### Exemplo: Contagem

```visualg
i <- 0
enquanto (i < 5) faca
   escreval("Número: ", i)
   i <- i + 1  // Importante!
fimenquanto
```

> Se esquecer o `i <- i + 1`, vira um **Loop Infinito**! 😱

---

## 3. Repita-Até (Do-While) 🛡️

- Testa a condição no **FINAL**. { .fragment }
- Executa **pelo menos uma vez**. { .fragment }
- Ótimo para menus ou validação. { .fragment }

---

### Sintaxe

```visualg
repita
   // Comandos
ate (condicao)
```

**Atenção**: No VisualG/Portugol, ele repete *até* a condição ser verdadeira (ou seja, enquanto for falsa). Em outras linguagens (C, Java), é *enquanto* for verdadeira.

---

### Exemplo: Senha Correta 🔒

```visualg
repita
   escreva("Digite a senha: ")
   leia(senha)
ate (senha == "1234")
```

---

## 4. Para (For) 🎯

- Quando sabemos **exatamente** quantas vezes repetir. { .fragment }
- Agrupa tudo numa linha só: { .fragment }
    1.  **Início** (Onde começa) { .fragment }
    2.  **Fim** (Onde termina) { .fragment }
    3.  **Passo** (De quanto em quanto) { .fragment }

---

### Sintaxe

```visualg
para i de 1 ate 10 passo 1 faca
   escreva(i)
fimpara
```

- **i**: Variável contadora. { .fragment }
- **1**: Valor inicial. { .fragment }
- **10**: Valor final. { .fragment }
- **1**: Incremento. { .fragment }

---

### Exemplo: Contagem Regressiva 🚀

```visualg
para i de 10 ate 0 passo -1 faca
   escreval(i)
fimpara
escreval("FOGO!")
```

---

## 5. Controle de Fluxo (Interrompa) 🛑

- Sai do loop imediatamente. { .fragment }
- Útil para parar buscas ou sair de menus. { .fragment }

```visualg
enquanto (verdadeiro) faca
   se (botao == "Sair") entao
      interrompa
   fimse
fimenquanto
```

---

## 6. O Teste de Mesa 🧠

Como debugar mentalmente?

1.  Crie uma tabela com as variáveis. { .fragment }
2.  Simule linha por linha. { .fragment }
3.  Anote as mudanças. { .fragment }

| Passo | i | Saída |
| :--- | :--- | :--- |
| 1 | 0 | - |
| 2 | 0 | "0" |
| 3 | 1 | - |
| ... | ... | ... |

---

## Comparativo ⚖️

| Estrutura | Quando usar? |
| :--- | :--- |
| **Enquanto** | Não sei quantas vezes vai repetir. |
| **Repita** | Tenho que executar pelo menos 1 vez. |
| **Para** | Sei exatamente o número de repetições. |

---

## Exercício Rápido ⚡

**Tabuada do 7**

1.  Use um `para`. { .fragment }
2.  De 1 até 10. { .fragment }
3.  Mostre `7 x i = resultado`. { .fragment }

---

## Resumo ✅

- **Loops** economizam tempo. { .fragment }
- **Cuidado** com Loops Infinitos. { .fragment }
- Escolha a estrutura certa para o problema. { .fragment }

---

## Próxima Aula 🚀

- E para guardar 50 notas de alunos? { .fragment }
- Criar 50 variáveis? `n1, n2, n3...`? 😫 { .fragment }
- **Vetores (Arrays)**: A solução elegante. { .fragment }

👉 **Tarefa**: Fazer a Tabuada e o Primo!