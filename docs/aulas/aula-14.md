## 🐦 Linguagem Dart

**Dart** é uma linguagem de programação moderna, flexível e otimizada, desenvolvida pelo Google. É a linguagem utilizada pelo framework Flutter.

### 📊 Tipos de Dados e Variáveis em Dart

Dart é uma linguagem **estaticamente tipada**, mas possui um poderoso sistema de **inferência de tipo** com a palavra-chave `var`.

  * `var`: Declara uma variável cujo tipo é inferido pelo compilador. Uma vez inferido, o tipo não pode mudar.
  * `final`: Declara uma variável que só pode ser definida uma vez (constante em tempo de execução).
  * `const`: Declara uma variável que é uma constante em tempo de compilação.

| Significado | Tipo em Dart | Observação |
| :--- | :--- | :--- |
| Número Inteiro | `int` | Números inteiros sem parte decimal. |
| Número de Ponto Flutuante | `double` | Números com casas decimais. |
| Texto | `String` | Uma sequência de caracteres, declarada com aspas simples ou duplas. |
| Valor Lógico | `bool` | Aceita apenas os valores `true` ou `false`. |
| Listas (Arrays) | `List` | Uma coleção ordenada de itens. Ex: `List<int>`. |
| Mapas | `Map` | Uma coleção de pares chave-valor. Ex: `Map<String, int>`. |

### 📝 Declaração e Saída de Dados

Em Dart, a interpolação de strings é a maneira mais comum de formatar texto. A função `print()` é usada para depuração e imprime no console.

```dart
// A função print() é usada para depuração e imprime no console de depuração.
void VariaveisExemplo() {
  final String nome = "Rafael Mendes"; // 'final' porque o nome não mudará.
  var idade = 25; // O tipo 'int' é inferido.
  var altura = 1.80; // O tipo 'double' é inferido.
  var isDesenvolvedor = true; // O tipo 'bool' é inferido.

  // Usando interpolação de string ($) para formatar a saída.
  print('NOME = $nome');
  print('IDADE = $idade');
  // Para formatar um double, podemos usar o método .toStringAsFixed().
  print('ALTURA = ${altura.toStringAsFixed(2)}');
  print('É DESENVOLVEDOR? = $isDesenvolvedor');
}
```

### 🔢 Operadores

#### Operadores Aritméticos

| Operador | Significado |
| :---: | :--- |
| `+` | Adição |
| `-` | Subtração |
| `*` | Multiplicação |
| `/` | Divisão |
| `~/` | Divisão inteira |
| `%` | Resto da divisão (módulo) |

#### Operadores de Igualdade e Relacionais

| Operador | Significado |
| :---: | :--- |
| `==` | Igual a |
| `!=` | Diferente de |
| `>` | Maior que |
| `<` | Menor que |
| `>=` | Maior ou igual a |
| `<=` | Menor ou igual a |

#### Operadores Lógicos

| Operador | Significado |
| :---: | :--- |
| `&&` | E |
| `||` | OU |
| `!` | NÃO |

#### Operadores Especiais de Dart

  * `??` (Null Coalescing): `var nome = nomeDoUsuario ?? "Convidado";` (Se `nomeDoUsuario` for nulo, use "Convidado").
  * `?.` (Null-aware access): `print(usuario?.email);` (Acesse `email` somente se `usuario` não for nulo, senão retorne `null`).

### 🔀 Estruturas de Controle

#### Estrutura Condicional (`if/else`)

```dart
var idade = 25;
if (idade >= 18) {
  print("É maior de idade.");
} else {
  print("É menor de idade.");
}
```

#### Estruturas de Repetição

**`for` (Laço Clássico):**

```dart
for (int i = 1; i <= 5; i++) {
  print('Número: $i');
}
```

**`for-in` (Para Coleções):**

```dart
var nomes = ['Rafael', 'Helena', 'Gabriel'];
for (var nome in nomes) {
  print(nome);
}
```

### 📏 Estruturas de Dados (Listas e Mapas)

#### Listas

As listas em Dart são o equivalente a arrays ou vetores.

```dart
// Cria uma lista de inteiros.
var numeros = <int>[10, 20, 30];
// Adiciona um novo elemento.
numeros.add(40);
// Acessa um elemento pelo índice.
print(numeros[1]); // Imprime 20
```

#### Mapas

Mapas são coleções de pares chave-valor.

```dart
var pontuacoes = <String, int>{
  'Rafael': 100,
  'Helena': 95,
};
// Adiciona um novo par.
pontuacoes['Gabriel'] = 98;
// Acessa um valor pela chave.
print(pontuacoes['Rafael']); // Imprime 100
```

---

### [ricardotecpro.github.io](https://ricardotecpro.github.io/)
## 🐦 Framework Flutter

**Flutter** é um toolkit de UI (Interface de Usuário) de código aberto, também do Google, que utiliza a linguagem Dart para construir aplicativos compilados de forma nativa para mobile, web, desktop e sistemas embarcados a partir de um único código-base. Em resumo: **Dart é a linguagem, Flutter é o framework** para construir a interface.

### 🛠️ Instalação e Configuração do Ambiente

Para desenvolver com Flutter, você precisa instalar o **Flutter SDK (Software Development Kit)**, que já inclui o Dart SDK.

1.  **Instale o Flutter SDK**: Acesse o [site oficial do Flutter](https://flutter.dev/docs/get-started/install) e siga o guia de instalação para o seu sistema operacional. O processo envolve baixar um arquivo, descompactá-lo e adicionar a pasta `bin` do Flutter ao `PATH` do seu sistema. Execute `flutter doctor` para verificar se há dependências faltando.

2.  **Configure uma IDE**:

      * **Visual Studio Code (Recomendado)**: Instale a extensão **"Flutter"**.
      * **Android Studio**: Instale o plugin **"Flutter"** através do menu de configurações.

### 🚀 Seu Primeiro Aplicativo Flutter

1.  **Crie um novo projeto**: No terminal, execute `flutter create meu_app`.
2.  **Entre no diretório**: `cd meu_app`.
3.  **Abra o projeto na IDE**. O arquivo principal é o `lib/main.dart`.
4.  Substitua o conteúdo de `lib/main.dart` pelo código de "Olá, Mundo":

<!-- end list -->

```dart
// Importa o pacote principal do Flutter para widgets do Material Design.
import 'package:flutter/material.dart';

// A função main() é o ponto de entrada de todo aplicativo Flutter.
void main() {
  // runApp() infla o widget principal e o anexa à tela.
  runApp(const MeuApp());
}

// Em Flutter, "tudo é um widget". Este é o widget raiz do seu aplicativo.
class MeuApp extends StatelessWidget {
  const MeuApp({super.key});

  @override
  Widget build(BuildContext context) {
    // MaterialApp é um widget que fornece funcionalidades básicas de um app.
    return MaterialApp(
      // Scaffold é um layout básico para uma tela de app Material.
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Meu Primeiro App'),
        ),
        // Center centraliza seu widget filho.
        body: const Center(
          // Text é o widget para exibir texto.
          child: Text('Olá, Universo Flutter!'),
        ),
      ),
    );
  }
}
```

5.  **Execute o aplicativo**: Pressione `F5` no VS Code ou clique no botão "Run" no Android Studio.

### 📥 Entrada de Dados em Flutter (Widgets Interativos)

A entrada de dados em Flutter é recebida através da interação do usuário com widgets como o `TextField`. Este processo geralmente envolve o uso de um **`StatefulWidget`** para gerenciar o estado da interface.

```dart
class TelaDeEntrada extends StatefulWidget {
  const TelaDeEntrada({super.key});

  @override
  State<TelaDeEntrada> createState() => _TelaDeEntradaState();
}

class _TelaDeEntradaState extends State<TelaDeEntrada> {
  // Um controller para ler e manipular o texto do TextField.
  final _controller = TextEditingController();
  String _nomeDigitado = "";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            // Widget para entrada de texto.
            TextField(
              controller: _controller,
              decoration: const InputDecoration(labelText: 'Digite seu nome'),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                // Atualiza o estado da tela para exibir o nome digitado.
                setState(() {
                  _nomeDigitado = _controller.text;
                });
              },
              child: const Text('Saudação'),
            ),
            const SizedBox(height: 20),
            Text('Olá, $_nomeDigitado!'),
          ],
        ),
      ),
    );
  }
}
```

### 🐞 Depuração (Debugging) em Flutter

As ferramentas de depuração do Flutter são um de seus pontos mais fortes.

  * **Hot Reload (Recarga Rápida)**: Aplica as mudanças no código da UI em seu aplicativo **em menos de um segundo**, sem perder o estado atual do app.
  * **Hot Restart (Reinício Rápido)**: Reinicia o aplicativo do zero, limpando o estado.
  * **Depuração com Breakpoints**: Adicione breakpoints no seu código clicando na margem da IDE e inicie em modo de depuração (`F5` no VS Code).
  * **Flutter DevTools**: Uma suíte de ferramentas que rodam no navegador, permitindo inspecionar a árvore de widgets, analisar performance, uso de memória e muito mais.

---

### [ricardotecpro.github.io](https://ricardotecpro.github.io/)
