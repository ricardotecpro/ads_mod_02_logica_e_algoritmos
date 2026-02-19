# Aula 13 - Python e Ciência de Dados 🐍

---

## Agenda 📅

1.  Por que Python?
2.  Sintaxe Limpa
3.  Estruturas de Dados Poderosas
4.  Modo Interativo (REPL) vs Scripts
5.  O Ecossistema de Data Science

---

## 1. Por que Python? 🚀

- **Legibilidade**: Parece inglês.
- **Produtividade**: Menos linhas, mais resultado.
- **Ecossistema**: IA, Data Science, Web, Automação.
- Não é o mais rápido (em CPU), mas é o mais rápido para **desenvolver**.

---

## 2. Sintaxe Limpa ✨

Esqueça `{}` e `;`.

- **Indentação** (espaços) define os blocos.
- Força o código a ser organizado.

```python
if idade >= 18:
    print("Maior")
else:
    print("Menor")
```

---

## 3. Estruturas de Dados 🧱

Em vez de Arrays e Matrizes chatos de declarar, temos **Listas** e **Dicionários**.

---

### Listas (Arrays Turbinados)

```python
frutas = ["Maçã", "Banana", "Uva"]
print(frutas[0]) # Maçã
frutas.append("Pera") # Adiciona no fim
```

---

### Dicionários (Chave-Valor) 🔑

Como um JSON ou um Objeto.

```python
pessoa = {
    "nome": "Ana",
    "idade": 25,
    "tech": ["Python", "SQL"]
}
print(pessoa["nome"])
```

---

### Visualizando (Mermaid)

```mermaid
graph LR;
    subgraph Lista [Lista: Compras]
    L0[0: Maçã] --- L1[1: Banana] --- L2[2: Uva]
    end
    
    subgraph Dicionario [Dicionário: Pessoa]
    D1[Chave: 'Nome'\nValor: 'Ana'] --- D2[Chave: 'Idade'\nValor: 25]
    end
    
    style Lista fill:#bbf;
    style Dicionario fill:#f9f;
```

---

## 4. Modos de Execução ⚙️

1.  **REPL (Interativo)**:
    - Digite `python` no terminal.
    - Teste comandos na hora. `2 + 2`.
    - Ótimo para aprender.

2.  **Scripts (`.py`)**:
    - Arquivos de texto com código.
    - `python meu_script.py`.
    - Para programas reais.

---

## 5. O Ecossistema de Dados 📊

Por que Data Science ama Python? **Bibliotecas**.

1.  **Pandas**: O "Excel" do programador. Manipula milhões de linhas.
2.  **Matplotlib**: Cria gráficos (Barras, Linhas, Pizza).
3.  **TensorFlow/PyTorch**: Inteligência Artificial.

---

### Exemplo Pandas 🐼

```python
import pandas as pd

# Ler uma planilha inteira
tabela = pd.read_csv("vendas.csv")

# Calcular totais
print(tabela["valor"].sum())
```

---

## Exercício Rápido ⚡

**Análise de Notas**

1.  Crie uma lista com 4 notas: `[6.0, 7.5, 9.0, 5.5]`.
2.  Use `sum(lista)` e `len(lista)` para calcular a média.
3.  Se média > 6, imprima "Aprovado".

```python
notas = [6.0, 7.5, 9.0, 5.5]
media = sum(notas) / len(notas)
# Complete...
```

---

## Resumo ✅

- Python é a linguagem da prototipagem e dos dados.
- **Indentação** é regra.
- **Bibliotecas** fazem o trabalho pesado.

---

## Próxima Aula 🚀

- E quando performance é tudo?
- Sistemas que não podem travar.
- **Rust e Go**: As linguagens da Cloud e Sistemas.

👉 **Tarefa**: Instalar Python e fazer o exercício da média!