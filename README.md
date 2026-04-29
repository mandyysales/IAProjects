# IAProjects
Descrição

Pasta pa projetos utilizando hugging face

O feedback_analyser recebe um texto e retorna:
Sentimento (positivo, negativo ou neutro)
Categoria (bug, elogio, sugestão, dúvida)

## Tecnologias utilizadas
Python
Hugging Face Transformers

## Como funciona
1. Análise de sentimento

Utiliza o pipeline:
pipeline("sentiment-analysis")
Esse pipeline usa um modelo pré-treinado para identificar o sentimento do texto.

2. Classificação de categoria

Utiliza:
pipeline("zero-shot-classification")
Esse método permite classificar textos sem necessidade de treinamento específico, usando apenas labels definidas pelo usuário.

Labels usadas:

bug
elogio
sugestão
dúvida

## ▶️ Como executar

Todos os codigos podem ser rodados usando colab

