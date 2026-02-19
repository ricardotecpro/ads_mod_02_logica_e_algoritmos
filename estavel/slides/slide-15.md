# Aula 15 - Desenvolvimento Mobile 📱

---

## Agenda 📅

1.  O Ecossistema Mobile { .fragment }
2.  Nativo vs Multiplataforma { .fragment }
3.  Dart e Flutter (Google) { .fragment }
4.  Árvore de Widgets { .fragment }
5.  Kotlin (Android Nativo) { .fragment }

---

## 1. O Mundo Mobile 🌍

Dois gigantes dominam o mercado.

- **Android (Google)**: ~70% do mercado mundial. Aberto. Baseado em Linux/Java. { .fragment }
- **iOS (Apple)**: ~29% do mercado. Fechado. Hardware Premium. { .fragment }

---

## 2. Abordagens de Desenvolvimento 🛠️

Como criar apps para eles?

1.  **Nativo**: { .fragment }
    - Performance Máxima. { .fragment }
    - Acesso total ao hardware (GPS, Bluetooth). { .fragment }
    - **Problema**: Precisa fazer 2 vezes (Kotlin para Android, Swift para iOS). { .fragment }

2.  **Multiplataforma**: { .fragment }
    - Escreve uma vez, roda nos dois. { .fragment }
    - Flutter (Dart) ou React Native (JS). { .fragment }
    - **Vantagem**: Velocidade de entrega. { .fragment }

---

## 3. Flutter e Dart 💙

- **Dart**: A linguagem (parece Java + JS). { .fragment }
- **Flutter**: O Kit de Ferramentas (UI Toolkit). { .fragment }
- Renderiza pixels direto na tela (como um jogo). { .fragment }

---

### Tudo é um Widget 🧱

Botão é widget. Texto é widget. Layout é widget.

```mermaid
graph TD;
    App[MaterialApp] --> Home["Tela Principal"];
    Home --> AppBar[Barra Superior];
    Home --> Body[Corpo];
    Body --> Center;
    Center --> Button["Botão Clique"];
    
    style App fill:#f9f;
```

---

### Código Flutter Básico

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    home: Scaffold(
      appBar: AppBar(title: Text("Meu App")),
      body: Center(child: Text("Olá Mundo!")),
    ),
  ));
}
```

---

## 4. O Estado (State) ⚡

Apps são interativos.
Se o usuário clica, a tela muda.

- **StatelessWidget**: Estático (Ícone, Texto). { .fragment }
- **StatefulWidget**: Dinâmico (Checkbox, Contador). { .fragment }

---

### Ciclo de Vida do Estado

```mermaid
graph LR;
    User["Usuário Clica"] --> Acao[setState];
    Acao --> Build[Reconstruir Tela];
    Build --> UI[Nova UI];
```

---

## 5. Kotlin (Android Nativo) 🤖

Para quando você precisa de poder bruto.

- Oficial do Google. { .fragment }
- 100% Compatível com Java. { .fragment }
- Conciso e seguro (sem NullPointerException). { .fragment }

```kotlin
fun main() {
    val nome = "Android"
    println("Olá, $nome!")
}
```

---

## Termynal: Criando App 📱

<div data-termynal class="termy">
    <span data-ty="input">flutter create meu_app</span>
    <span data-ty="progress">Criando arquivos...</span>
    <span data-ty="input">flutter run</span>
    <span data-ty="progress">Compilando APK...</span>
    <span data-ty>App rodando no Emulador!</span>
</div>

---

## Resumo ✅

- **Nativo**: Melhor performance, mais trabalho. { .fragment }
- **Multiplataforma**: Menor custo, velocidade. { .fragment }
- **Flutter**: Desenha a tela do zero. { .fragment }
- **Widgets**: Blocos de construção. { .fragment }

---

## Próxima Aula 🚀

- Sair do Cliente (Celular). { .fragment }
- Voltar para o Servidor (Backend). { .fragment }
- A tecnologia que roda 77% da Web. { .fragment }
- **PHP e Arquitetura MVC**. { .fragment }

👉 **Tarefa**: Rodar o "Counter App" do Flutter!