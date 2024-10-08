import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    emotion_values = [anger, disgust, fear, joy, sadness]
    dominant_emotion = max(emotion_values)
    labels = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'label': dominant_label,
        'score': dominant_emotion,
        'dominant_emotion': dominant_emotion
    }
