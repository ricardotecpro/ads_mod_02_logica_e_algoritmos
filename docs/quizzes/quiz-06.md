# Quiz 06 - Introdução

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. O que é um Vetor (Array)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Uma variável comum que guarda 1 valor</div>
  <div class="quiz-option" data-correct="true" data-feedback="Imagine um vetor como um armário com várias gavetas numeradas, todas guardando o mesmo tipo de "roupa".">Uma estrutura que guarda vários valores do mesmo tipo</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um desenho vetorial (SVG)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Uma seta da física
    ??? tip "Explicação"
        Imagine um vetor como um armário com várias gavetas numeradas, todas guardando o mesmo tipo de "roupa".</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Como identificamos cada "gaveta" de um vetor?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Pelo nome</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Pelo valor</div>
  <div class="quiz-option" data-correct="true" data-feedback="O índice é o número que indica a posição do dado. Ex: `notas[1]` pega a primeira nota.">Pelo Índice (Posição)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Pela cor
    ??? tip "Explicação"
        O índice é o número que indica a posição do dado. Ex: `notas[1]` pega a primeira nota.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Em algoritmos (VisualG), qual o primeiro índice geralmente?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">0</div>
  <div class="quiz-option" data-correct="true" data-feedback="Diferente de C ou Java (que começam em 0), o VisualG por padrão começa os vetores em 1.">1</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">-1</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">10
    ??? tip "Explicação"
        Diferente de C ou Java (que começam em 0), o VisualG por padrão começa os vetores em 1.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">1. 4. Se tenho `v: vetor [1..5]` e acesso `v[6]`, o que acontece?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O vetor cresce automaticamente</div>
  <div class="quiz-option" data-correct="true" data-feedback="Tentar acessar uma posição que não existe é um erro clássico que faz programas travarem.">Erro (Index Out of Bounds)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Retorna 0</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O PC desliga
    ??? tip "Explicação"
        Tentar acessar uma posição que não existe é um erro clássico que faz programas travarem.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Qual a melhor estrutura para percorrer um vetor inteiro?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Se...Senao</div>
  <div class="quiz-option" data-correct="true" data-feedback="O loop `Para` é ideal porque usamos o contador `i` como índice do vetor: `v[i]`.">Para (For)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Escolha...Caso</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Tentar adivinhar
    ??? tip "Explicação"
        O loop `Para` é ideal porque usamos o contador `i` como índice do vetor: `v[i]`.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. O que é "Bubble Sort"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um tipo de refrigerante</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um algoritmo de busca</div>
  <div class="quiz-option" data-correct="true" data-feedback="É um método simples de colocar números em ordem, onde os maiores "flutuam" para o fim da lista.">Um algoritmo de ordenação (bolha)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um tipo de variável
    ??? tip "Explicação"
        É um método simples de colocar números em ordem, onde os maiores "flutuam" para o fim da lista.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Posso guardar um "Nome" e uma "Idade" no mesmo vetor simples?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Sim, bagunçado</div>
  <div class="quiz-option" data-correct="true" data-feedback="Vetores tradicionais exigem que todos os elementos sejam do mesmo tipo (Ex: só inteiros).">Não, vetores são homogêneos (mesmo tipo)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Sim, se for em Javascript</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Depende do dia
    ??? tip "Explicação"
        Vetores tradicionais exigem que todos os elementos sejam do mesmo tipo (Ex: só inteiros).</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O que significa "Vetor Estático"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Que ele dá choque</div>
  <div class="quiz-option" data-correct="true" data-feedback="Significa que se você criou um vetor de 10 posições, não pode colocar 11 itens depois.">Que o tamanho é fixo (definido na criação)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Que ele muda de tamanho</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Que ele é radioativo
    ??? tip "Explicação"
        Significa que se você criou um vetor de 10 posições, não pode colocar 11 itens depois.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Para achar o MAIOR valor de um vetor, o que faço?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Ordeno e pego o último</div>
  <div class="quiz-option" data-correct="true" data-feedback="Esta é a técnica mais eficiente e didática para encontrar extremos em uma lista.">Percorro assumindo que o primeiro é o maior e comparo com os outros</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Somo tudo</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Pergunto ao usuário
    ??? tip "Explicação"
        Esta é a técnica mais eficiente e didática para encontrar extremos em uma lista.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Um vetor pode ter outros vetores dentro?</div>
  <div class="quiz-option" data-correct="true" data-feedback="Vetores de duas dimensões são chamados de Matrizes (LInhas e Colunas).">Sim (Matriz)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Não, impossível</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Apenas em computadores quânticos</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Talvez
    ??? tip "Explicação"
        Vetores de duas dimensões são chamados de Matrizes (LInhas e Colunas).</div>
  <div class="quiz-feedback"></div>
</div>

