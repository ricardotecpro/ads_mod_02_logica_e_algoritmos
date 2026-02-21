# Quiz 04 - Introdução

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Para que serva a estrutura `Se...Entao`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Para repetir código</div>
  <div class="quiz-option" data-correct="true" data-feedback="O bloco SE permite que o programa execute comandos apenas se uma condição for verdadeira.">Para tomar decisões baseadas em condições</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Para declarar variáveis</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Para imprimir na tela
    ??? tip "Explicação"
        O bloco SE permite que o programa execute comandos apenas se uma condição for verdadeira.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Qual operador verifica se dois valores são IGUAIS?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">=</div>
  <div class="quiz-option" data-correct="true" data-feedback="Cuidado! `=` geralmente atribui valor, enquanto `==` compara a igualdade entre dois itens.">== (ou = no VisualG dependendo da versão, mas == é padrão universal)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">===</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente."><>
    ??? tip "Explicação"
        Cuidado! `=` geralmente atribui valor, enquanto `==` compara a igualdade entre dois itens.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. O que o `Senao` faz?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Executa se a condição do Se for Verdadeira</div>
  <div class="quiz-option" data-correct="true" data-feedback="O SENÃO é o plano B: ele só roda se a primeira condição do SE não for atendida.">Executa se a condição do Se for Falsa</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Executa sempre</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Cancela o programa
    ??? tip "Explicação"
        O SENÃO é o plano B: ele só roda se a primeira condição do SE não for atendida.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Qual o resultado de `10 > 5 E 5 > 2`?</div>
  <div class="quiz-option" data-correct="true" data-feedback="No operador `E` (AND), as DUAS condições precisam ser verdade para o resultado ser verdade.">Verdadeiro</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Falso</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Erro</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">10
    ??? tip "Explicação"
        No operador `E` (AND), as DUAS condições precisam ser verdade para o resultado ser verdade.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Qual o resultado de `10 > 5 E 2 > 5`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Verdadeiro</div>
  <div class="quiz-option" data-correct="true" data-feedback="Como `2 > 5` é falso, o resultado final do `E` será falso, independente da primeira parte.">Falso</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Talvez</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">5
    ??? tip "Explicação"
        Como `2 > 5` é falso, o resultado final do `E` será falso, independente da primeira parte.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. O operador `OU` retorna Verdadeiro quando:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Todas as condições são verdadeiras</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Nenhuma condição é verdadeira</div>
  <div class="quiz-option" data-correct="true" data-feedback="O `OU` (OR) é pouco exigente: basta que uma das partes seja verdade para ele aceitar.">Pelo menos uma condição é verdadeira</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A primeira é falsa
    ??? tip "Explicação"
        O `OU` (OR) é pouco exigente: basta que uma das partes seja verdade para ele aceitar.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. O que é "Indentação"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Espaço em disco usado</div>
  <div class="quiz-option" data-correct="true" data-feedback="Indentar é essencial para organização humana. Ajuda a ver o que está dentro do SE ou do LOOP.">Recuo do código para indicar hierarquia/bloco</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Nome de variável inválido</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">erro de digitação
    ??? tip "Explicação"
        Indentar é essencial para organização humana. Ajuda a ver o que está dentro do SE ou do LOOP.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Para menus com muitas opções (1, 2, 3...), qual estrutura é melhor?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Muitos SEs encadeados</div>
  <div class="quiz-option" data-correct="true" data-feedback="O ESCOLHA organiza o código de forma mais limpa quando temos muitas opções fixas.">Escolha/Caso (Switch/Case)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Repita</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Vetor
    ??? tip "Explicação"
        O ESCOLHA organiza o código de forma mais limpa quando temos muitas opções fixas.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Como verificar se um número `x` é PAR?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">`x / 2 == 0`</div>
  <div class="quiz-option" data-correct="true" data-feedback="Se você divide por 2 e sobra 0, o número é múltiplo de 2, ou seja, é par.">`x % 2 == 0` (Resto da divisão é 0)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">`x % 2 == 1`</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">`x * 2`
    ??? tip "Explicação"
        Se você divide por 2 e sobra 0, o número é múltiplo de 2, ou seja, é par.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. A condição `SE (media >= 6)` inclui o 6?</div>
  <div class="quiz-option" data-correct="true" data-feedback="O operador `>=` significa "pelo menos aquele valor". Se fosse `>`, o 6 ficaria de fora.">Sim (Maior ou Igual)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Não (Apenas maior que 6)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Apenas se for inteiro</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Não sei
    ??? tip "Explicação"
        O operador `>=` significa "pelo menos aquele valor". Se fosse `>`, o 6 ficaria de fora.</div>
  <div class="quiz-feedback"></div>
</div>

