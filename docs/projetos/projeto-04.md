# Projeto 04 - Calculadora IMC (Milestone 1 Final) ⚖️

## O Desafio 🎯
O Ministério da Saúde precisa de um sistema rápido para triagem de pacientes baseada no IMC (Índice de Massa Corporal).

**Objetivo**: Integrar Variáveis, Entrada/Saída e Estruturas Condicionais em um programa útil.

## Requisitos Técnicos
1.  **Entrada**: Ler `peso` (kg) e `altura` (m).
2.  **Processamento**: Calcular `IMC = peso / (altura * altura)`.
3.  **Saída**: Classificar o resultado segundo a tabela:
    - Abaixo de 18.5: "Abaixo do Peço"
    - 18.5 a 24.9: "Peso Ideal"
    - 25 a 29.9: "Sobrepeso"
    - 30+: "Obesidade"

## Teste de Mesa (Exemplos)

| Peso (kg) | Altura (m) | IMC (Calculado) | Saída Esperada |
| :--- | :--- | :--- | :--- |
| 70 | 1.75 | 22.8 | Peso Ideal |
| 90 | 1.75 | 29.3 | Sobrepeso |
| 50 | 1.80 | 15.4 | Abaixo do Peso |

## Dicas 💡
- Cuidado com o ponto decimal (use `.` ou `,` dependendo da configuração do seu sistema/linguagem).
- Use `Se...Senao Se` encadeados.

## Ferramenta
- VisualG (Portugol).