# Quiz 14 - Introdução

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual o foco principal da linguagem Rust?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Facilidade de aprendizado</div>
  <div class="quiz-option" data-correct="true" data-feedback="Rust resolve o maior problema do C/C++: erros de memória que causam travamentos e furos de segurança.">Segurança de Memória e Performance (sem Garbage Collector)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Desenvolvimento Web Frontend</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Scripts simples
    ??? tip "Explicação"
        Rust resolve o maior problema do C/C++: erros de memória que causam travamentos e furos de segurança.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. O que é o "Borrow Checker" (Verificador de Empréstimo) do Rust?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um sistema de empréstimo bancário</div>
  <div class="quiz-option" data-correct="true" data-feedback="É como um bibliotecário rigoroso que só deixa você usar a memória se garantir que vai devolvê-la intacta.">O compilador garantindo que ninguém acesse memória inválida</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Uma biblioteca de matemática</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um erro comum
    ??? tip "Explicação"
        É como um bibliotecário rigoroso que só deixa você usar a memória se garantir que vai devolvê-la intacta.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Go (Golang) foi criado por qual empresa?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Facebook</div>
  <div class="quiz-option" data-correct="true" data-feedback="O Google criou o Go para resolver seus próprios desafios de servidores gigantescos e muitos programadores trabalhando juntos.">Google</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Amazon</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Microsoft
    ??? tip "Explicação"
        O Google criou o Go para resolver seus próprios desafios de servidores gigantescos e muitos programadores trabalhando juntos.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. O que são Goroutines em Go?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Rotinas de dança</div>
  <div class="quiz-option" data-correct="true" data-feedback="Você pode rodar milhares de Goroutines simultaneamente sem pesar no computador, algo difícil em outras linguagens.">Threads ultra-leves para concorrência</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Funções matemáticas</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Erros de compilação
    ??? tip "Explicação"
        Você pode rodar milhares de Goroutines simultaneamente sem pesar no computador, algo difícil em outras linguagens.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. A ferramenta oficial de gerenciamento de pacotes do Rust é:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">npm</div>
  <div class="quiz-option" data-correct="true" data-feedback="O Cargo cuida de tudo no Rust: cria o projeto, baixa bibliotecas (crates) e compila seu código.">cargo</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">pip</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">maven
    ??? tip "Explicação"
        O Cargo cuida de tudo no Rust: cria o projeto, baixa bibliotecas (crates) e compila seu código.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Go usa ponto-e-vírgula `;` obrigatório no final da linha?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Sim</div>
  <div class="quiz-option" data-correct="true" data-feedback="O Go foi desenhado para ter um código limpo e minimalista, eliminando símbolos desnecessários para a leitura humana.">Não (o compilador insere se omitido)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Apenas em loops</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Depende do editor
    ??? tip "Explicação"
        O Go foi desenhado para ter um código limpo e minimalista, eliminando símbolos desnecessários para a leitura humana.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Qual linguagem está sendo introduzida no Kernel do Linux?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Java</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Python</div>
  <div class="quiz-option" data-correct="true" data-feedback="Pela primeira vez em décadas, o Kernel do Linux aceitou uma nova linguagem (Rust) para trazer mais segurança aos componentes do sistema.">Rust</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">C#
    ??? tip "Explicação"
        Pela primeira vez em décadas, o Kernel do Linux aceitou uma nova linguagem (Rust) para trazer mais segurança aos componentes do sistema.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Rust permite usar valores "NULL" livremente?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Sim</div>
  <div class="quiz-option" data-correct="true" data-feedback="Rust obriga você a tratar o caso de um valor ser "nada", evitando o famoso erro de ponteiro nulo.">Não, usa o tipo Option<T> para segurança</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Sim, mas avisa</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Depende da versão
    ??? tip "Explicação"
        Rust obriga você a tratar o caso de um valor ser "nada", evitando o famoso erro de ponteiro nulo.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Para comunicação entre Goroutines, Go utiliza:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Emails</div>
  <div class="quiz-option" data-correct="true" data-feedback="O lema do Go é: "Não se comunique compartilhando memória; compartilhe memória se comunicando (via canais)".">Channels (Canais)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Variáveis globais inseguras</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Arquivos de texto
    ??? tip "Explicação"
        O lema do Go é: "Não se comunique compartilhando memória; compartilhe memória se comunicando (via canais)".</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Ambas as linguagens (Rust e Go) são:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Interpretadas</div>
  <div class="quiz-option" data-correct="true" data-feedback="Ao contrário do Python/JS, elas geram um arquivo executável que não precisa de um interpretador para rodar.">Compiladas (Geram binário nativo)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Apenas para Windows</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Lentas
    ??? tip "Explicação"
        Ao contrário do Python/JS, elas geram um arquivo executável que não precisa de um interpretador para rodar.</div>
  <div class="quiz-feedback"></div>
</div>

