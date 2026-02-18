# Projeto 12 - API Climática (Milestone 3) 🌦️

## O Desafio 🎯
Você trabalha em uma StartUp de Agricultura. Os fazendeiros precisam saber a previsão do tempo para planejar a colheita.

**Objetivo**: Consumir dados reais da internet (JSON) e processar com C# e LINQ.

## Requisitos Técnicos
1.  **Linguagem**: C# (.NET Core).
2.  **Dados**: Simule uma resposta JSON de API (ou use uma real se souber `HttpClient`).
    - Lista de objetos `Previsao` (Dia, Temperatura, Chuva?).
3.  **Funcionalidades (LINQ)**:
    - `Filtro`: Mostrar dias com Chuva = true.
    - `Ordenação`: Mostrar dias mais quentes primeiro.
    - `Média`: Qual a temperatura média da semana?

## Exemplo de Dados (Mock)
```csharp
var previsoes = new List<Previsao> {
    new Previsao { Dia = "Seg", Temp = 30, Chuva = true },
    new Previsao { Dia = "Ter", Temp = 28, Chuva = false },
    new Previsao { Dia = "Qua", Temp = 35, Chuva = false }
};
```

## Consultas Esperadas
- "Dias de Chuva: Seg"
- "Temp Máxima: 35 (Qua)"
- "Média: 31.0"

## Entrega 📦
- Código Fonte `.cs` (Console Application).