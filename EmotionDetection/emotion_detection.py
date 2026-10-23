import requests


def emotion_detector(text_to_analyze):
    empty_result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    if not text_to_analyze or not text_to_analyze.strip():
        return empty_result.copy()

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"
    }

    try:
        response = requests.post(
            url,
            json={"raw_document": {"text": text_to_analyze}},
            headers=headers,
            timeout=15
        )

        if response.status_code == 400:
            return empty_result.copy()

        response.raise_for_status()
        data = response.json()
        emotions = data["emotionPredictions"][0]["emotion"]

        result = {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"]
        }

        result["dominant_emotion"] = max(
            result, key=result.get
        )

        return result

    except (
        requests.RequestException,
        KeyError,
        IndexError,
        TypeError,
        ValueError
    ):
        return empty_result.copy()