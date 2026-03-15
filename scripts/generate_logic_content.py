import os

titles = [
    "Conteúdo do Curso",
    "Introdução à Programação",
    "Estrutura Sequencial",
    "Estrutura Condicional",
    "Estruturas Repetitivas",
    "Vetores",
    "Matrizes",
    "Funções",
    "Linguagem C",
    "Linguagem C++",
    "Linguagem Java",
    "Linguagem C#",
    "Linguagem Python",
    "Linguagem JavaScript",
    "Linguagem Rust",
    "Linguagem Dart"
]

base_dir = r"d:\SourceCode\REPOS\github.io\ads_mod_02_logica_e_algoritmos\docs"

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {path}")

def generate_slide_md(i, title):
    return f"""# {title}

---

## Tópicos da Aula

- Introdução ao tema
- Conceitos fundamentais
- Exemplos práticos
- Exercícios de fixação

---

## Conceito Chave

> Definição importante sobre {title}.

---

## Exemplo Prático

```
// Exemplo de código ou algoritmo
escreva("Olá mundo!")
```

---

## Conclusão

- Resumo do que aprendemos
- Próximos passos
"""

def generate_slide_html(i, title):
    # Keep the existing structure but update title
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aula {i:02d} - {title}</title>
    
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/dist/reset.css">
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/dist/reveal.css">
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/dist/theme/black.css">
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/plugin/highlight/monokai.css">
    <script src="https://unpkg.com/reveal.js@4.5.0/dist/reveal.js"></script>
    <script src="https://unpkg.com/reveal.js@4.5.0/plugin/markdown/markdown.js"></script>
    <script src="https://unpkg.com/reveal.js@4.5.0/plugin/highlight/highlight.js"></script>
    <script src="https://unpkg.com/reveal.js@4.5.0/plugin/notes/notes.js"></script>
    <script>
        Reveal.initialize({
            hash: true,
            slideNumber: 'c/t',
            showSlideNumber: 'all',
            controls: true,
            progress: true,
            plugins: [ RevealMarkdown, RevealHighlight, RevealNotes ]
        });
    </script>
</body>
</html>
"""

def generate_quiz(i, title):
    return f"""# Quiz {i:02d} - {title}

<link rel="stylesheet" href="../../assets/css/quiz.css">
<script src="../../assets/js/quiz.js" defer></script>

<div class="quiz-container">
  <div class="quiz-item" id="q1">
    <div class="quiz-question">1. Pergunta sobre {title}?</div>
    <div class="quiz-options">
      <div class="quiz-option" data-correct="true" data-feedback="Correto!">
        <span class="option-letter">A)</span> Resposta Correta.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">B)</span> Resposta Incorreta.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">C)</span> Outra opção.
      </div>
    </div>
    <div class="quiz-feedback"></div>
  </div>
</div>
"""

def generate_exercise(i, title):
    return f"""# Exercícios - Aula {i:02d}: {title}

## 🛠 Prática

1. **Exercício Teórico**:
   - Explique com suas palavras o conceito de {title}.

2. **Exercício Prático**:
   - Implemente um algoritmo simples relacionado a {title}.
   - Teste com diferentes entradas.

"""

def generate_project(i, title):
    return f"""# Projeto - Aula {i:02d}: {title}

## 🚀 Desafio

Desenvolva um pequeno projeto aplicando os conceitos de {title}.

### Requisitos:
1. Deve utilizar o conceito principal da aula.
2. Deve ser funcional e compilável/executável.
3. Documente seu código.

### Sugestão:
Crie um programa que resolva um problema do cotidiano usando {title}.
"""

def main():
    for idx, title in enumerate(titles):
        i = idx + 1
        
        # Slides
        ensure_dir(os.path.join(base_dir, "slides"))
        write_file(os.path.join(base_dir, "slides", f"slide-{i:02d}.md"), generate_slide_md(i, title))
        write_file(os.path.join(base_dir, "slides", f"slide-{i:02d}.html"), generate_slide_html(i, title))
        
        # Quizzes
        ensure_dir(os.path.join(base_dir, "quizzes"))
        write_file(os.path.join(base_dir, "quizzes", f"quiz-{i:02d}.md"), generate_quiz(i, title))
        
        # Exercicios
        ensure_dir(os.path.join(base_dir, "exercicios"))
        write_file(os.path.join(base_dir, "exercicios", f"exercicio-{i:02d}.md"), generate_exercise(i, title))
        
        # Projetos
        ensure_dir(os.path.join(base_dir, "projetos"))
        write_file(os.path.join(base_dir, "projetos", f"projeto-{i:02d}.md"), generate_project(i, title))

if __name__ == "__main__":
    main()
