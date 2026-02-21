# Quiz 09 - Introdução

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. A Linguagem C é conhecida como:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A linguagem mais fácil do mundo</div>
  <div class="quiz-option" data-correct="true" data-feedback="Criada em 1972, o C é a base de quase todos os sistemas operacionais modernos como Windows e Linux.">O Pai das Linguagens Modernas (Baixo Nível)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Uma linguagem apenas para Web</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Uma linguagem morta
    ??? tip "Explicação"
        Criada em 1972, o C é a base de quase todos os sistemas operacionais modernos como Windows e Linux.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. O que é a memória Stack (Pilha)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Memória lenta e gigante</div>
  <div class="quiz-option" data-correct="true" data-feedback="A Stack é onde ficam as variáveis de curta duração que o compilador gerencia automaticamente para nós.">Memória rápida para variáveis locais e funções</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O HD do computador</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A nuvem
    ??? tip "Explicação"
        A Stack é onde ficam as variáveis de curta duração que o compilador gerencia automaticamente para nós.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. O que é a memória Heap (Monte)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Memória organizada automaticamente</div>
  <div class="quiz-option" data-correct="true" data-feedback="O Heap é o "espaço livre" onde o programador decide quando alocar e quando liberar memória.">Memória dinâmica, gerenciada manualmente (malloc/free)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A memória da placa de vídeo</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O cache do processador
    ??? tip "Explicação"
        O Heap é o "espaço livre" onde o programador decide quando alocar e quando liberar memória.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. O que guarda um Ponteiro?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um valor inteiro</div>
  <div class="quiz-option" data-correct="true" data-feedback="Imagine o ponteiro como um papel com o endereço de uma casa escrito nele, em vez da casa em si.">O Endereço de Memória de outra variável</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um texto</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Uma imagem
    ??? tip "Explicação"
        Imagine o ponteiro como um papel com o endereço de uma casa escrito nele, em vez da casa em si.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Qual comando usamos para COMPILAR um código C no terminal (geralmente)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">run c</div>
  <div class="quiz-option" data-correct="true" data-feedback="O `gcc` (GNU Compiler Collection) é o compilador padrão da indústria para a linguagem C.">gcc arquivo.c -o saida</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">python arquivo.c</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">compile c
    ??? tip "Explicação"
        O `gcc` (GNU Compiler Collection) é o compilador padrão da indústria para a linguagem C.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Qual a principal diferença do C++ em relação ao C?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É mais lento</div>
  <div class="quiz-option" data-correct="true" data-feedback="O C++ "nasceu" como um C com Classes, permitindo organizar sistemas muito maiores e complexos.">Suporte a Orientação a Objetos (Classes)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Não usa ponteiros</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Não precisa compilar
    ??? tip "Explicação"
        O C++ "nasceu" como um C com Classes, permitindo organizar sistemas muito maiores e complexos.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. O que acontece se acessarmos um ponteiro inválido (NULL)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Nada</div>
  <div class="quiz-option" data-correct="true" data-feedback="O "Segfault" ocorre quando o programa tenta ler/escrever numa região de memória que não lhe pertence.">Segmentation Fault (O programa trava)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O computador reinicia</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O compilador corrige
    ??? tip "Explicação"
        O "Segfault" ocorre quando o programa tenta ler/escrever numa região de memória que não lhe pertence.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O que faz `#include <stdio.h>`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Inclui a biblioteca de gráficos</div>
  <div class="quiz-option" data-correct="true" data-feedback="O `stdio` (Standard Input Output) contém as funções `printf` (escrever) e `scanf` (ler).">Inclui a biblioteca padrão de Entrada e Saída (IO)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Inclui o Studio Code</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Inclui a internet
    ??? tip "Explicação"
        O `stdio` (Standard Input Output) contém as funções `printf` (escrever) e `scanf` (ler).</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. `int main()` deve retornar o que ao final com sucesso?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">1</div>
  <div class="quiz-option" data-correct="true" data-feedback="Retornar `0` para o Sistema Operacional significa: "Tudo correu bem, pode fechar o processo".">0</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">-1</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">"Fim"
    ??? tip "Explicação"
        Retornar `0` para o Sistema Operacional significa: "Tudo correu bem, pode fechar o processo".</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Por que aprender C/C++ hoje em dia?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Para fazer sites simples</div>
  <div class="quiz-option" data-correct="true" data-feedback="Aprender C te ensina a realidade física da memória e do processador, o que te torna um programador melhor em qualquer outra linguagem.">Para entender como o computador funciona e performance (Jogos, SO)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Porque é modinha</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Para scripts rápidos
    ??? tip "Explicação"
        Aprender C te ensina a realidade física da memória e do processador, o que te torna um programador melhor em qualquer outra linguagem.</div>
  <div class="quiz-feedback"></div>
</div>

