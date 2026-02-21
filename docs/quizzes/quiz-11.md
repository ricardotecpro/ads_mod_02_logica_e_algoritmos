# Quiz 11 - Introdução

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. O slogan do Java é "Write Once, Run Anywhere". O que permite isso?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O código fonte ASCII</div>
  <div class="quiz-option" data-correct="true" data-feedback="O código Java é compilado para Bytecode, que roda em qualquer sistema que tenha a JVM instalada.">A JVM (Java Virtual Machine)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O Windows</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A internet
    ??? tip "Explicação"
        O código Java é compilado para Bytecode, que roda em qualquer sistema que tenha a JVM instalada.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Um Objeto é uma instância de uma:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Função</div>
  <div class="quiz-option" data-correct="true" data-feedback="A Classe é o "molde" ou "planta baixa", e o Objeto é a "casa" construída a partir desse molde.">Classe</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Variável</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Matriz
    ??? tip "Explicação"
        A Classe é o "molde" ou "planta baixa", e o Objeto é a "casa" construída a partir desse molde.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual pilar da OO protege os dados sensíveis de uma classe?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Herança</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Polimorfismo</div>
  <div class="quiz-option" data-correct="true" data-feedback="Encapsular é "proteger dentro de uma cápsula", usando modificadores como `private` e métodos `get/set`.">Encapsulamento</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Abstração
    ??? tip "Explicação"
        Encapsular é "proteger dentro de uma cápsula", usando modificadores como `private` e métodos `get/set`.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Para herdar de uma classe em Java, usamos:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">implements</div>
  <div class="quiz-option" data-correct="true" data-feedback="`extends` (estende) indica que uma classe filha terá todas as características da classe pai.">extends</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">inherits</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">clone
    ??? tip "Explicação"
        `extends` (estende) indica que uma classe filha terá todas as características da classe pai.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. O que faz o Spring Boot?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Limpa o PC</div>
  <div class="quiz-option" data-correct="true" data-feedback="Ele revolucionou o Java ao automatizar tarefas chatas de configuração, permitindo focar apenas na lógica.">Facilita a criação de aplicações Java (Web/Microserviços) com configuração mínima</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Compila o código mais rápido</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É um jogo
    ??? tip "Explicação"
        Ele revolucionou o Java ao automatizar tarefas chatas de configuração, permitindo focar apenas na lógica.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. O métódo `public static void main(String[] args)` serve para:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Declarar variáveis</div>
  <div class="quiz-option" data-correct="true" data-feedback="É o "start" obrigatório. Sem o método `main`, o computador não sabe por onde começar a rodar seu App Java.">Ser o ponto de entrada (Início) da aplicação</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Imprimir na tela</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Conectar no banco
    ??? tip "Explicação"
        É o "start" obrigatório. Sem o método `main`, o computador não sabe por onde começar a rodar seu App Java.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. O Garbage Collector do Java serve para:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Coletar lixo eletrônico</div>
  <div class="quiz-option" data-correct="true" data-feedback="Diferente do C (onde você limpa a memória), o Java tem um "faxineiro" que cuida disso sozinho para você.">Limpar automaticamente memória RAM não utilizada</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Organizar arquivos</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Deletar vírus
    ??? tip "Explicação"
        Diferente do C (onde você limpa a memória), o Java tem um "faxineiro" que cuida disso sozinho para você.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O que é o Maven?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um tipo de café</div>
  <div class="quiz-option" data-correct="true" data-feedback="O Maven gerencia as bibliotecas que seu projeto precisa, baixando-as automaticamente da internet.">Um gerenciador de dependências e construção de projetos</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um editor de texto</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um banco de dados
    ??? tip "Explicação"
        O Maven gerencia as bibliotecas que seu projeto precisa, baixando-as automaticamente da internet.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Se eu tenho `Animal a = new Cachorro()`, isso é um exemplo de:</div>
  <div class="quiz-option" data-correct="true" data-feedback="Polimorfismo significa "muitas formas". Um objeto pode ser tratado como o tipo genérico da sua classe pai.">Polimorfismo</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Encapsulamento</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Erro</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Recursão
    ??? tip "Explicação"
        Polimorfismo significa "muitas formas". Um objeto pode ser tratado como o tipo genérico da sua classe pai.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Tipagem do Java é:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Fraca e Dinâmica</div>
  <div class="quiz-option" data-correct="true" data-feedback="Significa que os tipos são fixos e verificados rigorosamente pelo compilador, trazendo segurança.">Forte e Estática</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Opcional</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Inexistente
    ??? tip "Explicação"
        Significa que os tipos são fixos e verificados rigorosamente pelo compilador, trazendo segurança.</div>
  <div class="quiz-feedback"></div>
</div>

