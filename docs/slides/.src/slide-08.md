# Aula 08 - Modularização 🧩

---

## Agenda 📅

1.  Conceito de Módulos (Divide & Conquer)
2.  Procedimentos vs Funções
3.  Escopo de Variáveis (Locais x Globais)
4.  Parâmetros (Valor x Referência)
5.  Exemplos Práticos

---

## 1. Dividir para Conquistar ⚔️

Imagine construir um carro inteiro num bloco só. Impossível!
Nós montamos:
- Motor 🔧
- Rodas 🚗
- Vidros 🪟
E depois **juntamos**.

---

### Na Programação

- Não escreva 1000 linhas no `Inicio`.
- Quebre em pequenos blocos (**Módulos**).
- Cada módulo resolve **um problema específico**.

---

### Visualizando (Mermaid)

```mermaid
sequenceDiagram
    participant Principal
    participant Soma
    
    Principal->>Soma: Envia (5, 3)
    Note right of Soma: Calcula 5+3
    Soma-->>Principal: Retorna 8
    Principal->>Principal: Mostra 8
```

---

## 2. Tipos de Módulos 🛠️

Em Portugol, temos dois tipos principais.

1.  **Procedimentos**: Fazem uma ação, mas não devolvem valor matemático.
2.  **Funções**: Calculam e **RETORNAM** um valor.

---

### Procedimento (Ação)

Ex: `LimparTela()`, `MostrarMenu()`, `TocarSom()`.

```portugol
procedimento saudacao(nome : caractere)
inicio
   escreval("Olá, ", nome)
fimprocedimento
```
> Chamada: `saudacao("João")`

---

### Função (Cálculo)

Ex: `Raiz(x)`, `Soma(a,b)`, `Media(n1,n2)`.
Tem a palavra mágica **RETORNE**.

```portugol
funcao somar(a, b : inteiro) : inteiro
inicio
   retorne a + b
fimfuncao
```
> Chamada: `res <- somar(2, 3)`

---

## 3. Escopo de Variáveis 🏠

Onde minha variável vive?

- **Global**: Criada fora de tudo. Todo mundo vê. (Perigoso!).
- **Local**: Criada dentro da função. Só a função vê. (Seguro!).

---

### O Muro das Funções 🧱

Se eu crio `x` dentro de `somar`, o `Principal` **não sabe** quem é `x`.
Isso evita confusão!

---

## 4. Parâmetros 🚚

Como passar dados para a função?

1.  **Por Valor** (O padrão): Envia uma **CÓPIA**. Se a função mudar, o original não muda.
2.  **Por Referência** (`var`): Envia o **ENDEREÇO**. Se a função mudar, o original MUDA!

---

### Exemplo: Troca de Valores

Precisa ser por Referência!

```portugol
procedimento troca(var a, var b : inteiro)
inicio
   temp <- a
   a <- b
   b <- temp
fimprocedimento
```

---

## 5. Vantagens da Modularização ✅

1.  **Reutilização**: Escreve uma vez, usa 1000 vezes.
2.  **Organização**: Código limpo.
3.  **Facilidade de Manutenção**: Se o cálculo mudar, corrijo num lugar só.

---

## Projeto Final Módulo 1 🏆

**Sistema de Notas Completo**

- Use Vetores.
- Use Matrizes (se quiser).
- Use Funções para calcular média.
- Use Procedimentos para mostrar boletim.

---

## Resumo ✅

- Modularizar = Organizar.
- **Função** retorna valor. **Procedimento** faz ação.
- Variáveis **Locais** são protegidas.
- Use parâmetros para comunicar.

---

## Próxima Aula 🚀

- Fim da "Lógica Pura"!
- Vamos conhecer linguagens reais.
- **C e C++**: Os pais da programação moderna.
- Gerenciamento de Memória na unha!

👉 **Tarefa**: Refatore seus códigos antigos usando Funções!