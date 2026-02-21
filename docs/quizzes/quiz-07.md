# Quiz 07 - Introdução

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. O que é uma Matriz em programação?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O filme com Keanu Reeves</div>
  <div class="quiz-option" data-correct="true" data-feedback="Matrizes são "planilhas" de dados, organizadas em linhas e colunas.">Um vetor multidimensional (geralmente bidimensional, com linhas e colunas)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Uma impressora matricial</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um erro de sistema
    ??? tip "Explicação"
        Matrizes são "planilhas" de dados, organizadas em linhas e colunas.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Quantos índices eu preciso para acessar um elemento de uma Matriz 2D?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">1</div>
  <div class="quiz-option" data-correct="true" data-feedback="Como no Batalha Naval ou no Excel, você precisa de duas coordenadas: a linha e a coluna.">2 (Linha e Coluna)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">3</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">0
    ??? tip "Explicação"
        Como no Batalha Naval ou no Excel, você precisa de duas coordenadas: a linha e a coluna.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Se tenho `m[3,3]`, quantos elementos cabem no total?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">3</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">6</div>
  <div class="quiz-option" data-correct="true" data-feedback="O total de espaços em uma matriz é a multiplicação do número de linhas pelas colunas.">9 (3x3)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">12
    ??? tip "Explicação"
        O total de espaços em uma matriz é a multiplicação do número de linhas pelas colunas.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Em uma matriz, o que representam `i` e `j` geralmente?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Início e Janela</div>
  <div class="quiz-option" data-correct="true" data-feedback="É uma convenção matemática: `i` para o índice da linha e `j` para o índice da coluna.">Linha e Coluna</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Inteiro e Java</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Índio e Jaca
    ??? tip "Explicação"
        É uma convenção matemática: `i` para o índice da linha e `j` para o índice da coluna.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. O que é a Diagonal Principal de uma matriz Quadrada?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A primeira linha</div>
  <div class="quiz-option" data-correct="true" data-feedback="É a "linha torta" que vai do canto superior esquerdo ao canto inferior direito.">A linha onde i é igual a j (0,0; 1,1; 2,2...)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A última coluna</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A borda da matriz
    ??? tip "Explicação"
        É a "linha torta" que vai do canto superior esquerdo ao canto inferior direito.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Para percorrer uma matriz inteira, qual estrutura uso?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um Para simples</div>
  <div class="quiz-option" data-correct="true" data-feedback="O primeiro loop percorre as linhas, e para cada linha, o segundo loop percorre as colunas.">Dois Paras aninhados (um dentro do outro)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um Se dentro de um Enquanto</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Switch Case
    ??? tip "Explicação"
        O primeiro loop percorre as linhas, e para cada linha, o segundo loop percorre as colunas.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Uma imagem digital pode ser representada por uma Matriz?</div>
  <div class="quiz-option" data-correct="true" data-feedback="Cada pixel é uma posição na matriz. Filtros de imagem são, na verdade, cálculos matemáticos sobre matrizes.">Sim, pixels são pontos numa grade (R,G,B)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">No, imagem é mágica</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Apenas se for preto e branco</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Não, imagem é vetor
    ??? tip "Explicação"
        Cada pixel é uma posição na matriz. Filtros de imagem são, na verdade, cálculos matemáticos sobre matrizes.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. No jogo Batalha Naval, o tabuleiro é uma:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Lista</div>
  <div class="quiz-option" data-correct="true" data-feedback="Qualquer jogo que use grade (Batalha Naval, Xadrez, Jogo da Velha) usa matrizes por trás.">Matriz</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Pilha</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Fila
    ??? tip "Explicação"
        Qualquer jogo que use grade (Batalha Naval, Xadrez, Jogo da Velha) usa matrizes por trás.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Matriz Identidade tem:</div>
  <div class="quiz-option" data-correct="true" data-feedback="É uma matriz neutra na multiplicação de matrizes, similar ao número 1 na multiplicação comum.">1 na diagonal principal e 0 no resto</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Tudo 1</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Tudo 0</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Números aleatórios
    ??? tip "Explicação"
        É uma matriz neutra na multiplicação de matrizes, similar ao número 1 na multiplicação comum.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Matrizes tridimensionais (3D) existem?</div>
  <div class="quiz-option" data-correct="true" data-feedback="Chamamos isso de Tensor. É usado em vídeos (Matriz de quadros) e até em Inteligência Artificial.">Sim (Linha, Coluna, Profundidade)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Não, o limite é 2</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Apenas na NASA</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Sim, mas não servem para nada
    ??? tip "Explicação"
        Chamamos isso de Tensor. É usado em vídeos (Matriz de quadros) e até em Inteligência Artificial.</div>
  <div class="quiz-feedback"></div>
</div>

