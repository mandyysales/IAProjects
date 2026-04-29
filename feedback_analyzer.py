# feedback_analyzer.py
##Estudo hugging face
from transformers import pipeline

# Pipeline de sentimento
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

# Pipeline de classificação zero-shot
category_pipeline = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

# Labels possíveis
CATEGORIES = ["bug", "elogio", "sugestão", "dúvida"]


def analyze_feedback(texto):

    # --- Sentimento ---
    sentiment_result = sentiment_pipeline(texto)[0]

    label = sentiment_result["label"]
    score = sentiment_result["score"]

    ##converter deestrelas para palavras
    if "1" in label or "2" in label:
        sentimento = "negativo"
    elif "3" in label:
        sentimento = "neutro"
    else:
        sentimento = "positivo"

    # --- Categoria ---
    category_result = category_pipeline(
        texto,
        candidate_labels=CATEGORIES
    )

    categoria = category_result["labels"][0]
    confidence = category_result["scores"][0]

    return {
        "texto": texto,
        "sentimento": sentimento,
        "score_sentimento": score,
        "categoria": categoria,
        "score_categoria": confidence
    }


if __name__ == "__main__":
    exemplos = [
        "O app travou quando tentei fazer login",
        "Adorei a interface, muito bonita!",
        "Vocês poderiam adicionar modo escuro",
        "Como faço para resetar minha senha?"
    ]

    for texto in exemplos:
        resultado = analyze_feedback(texto)
        print("\n====================")
        print(f"Texto: {resultado['texto']}")
        print(f"Sentimento: {resultado['sentimento']}")
        print(f"Categoria: {resultado['categoria']}")