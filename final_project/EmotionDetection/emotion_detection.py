import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    return response.text

def emotion_predictor(text_to_analyse):
    response = emotion_detector(text_to_analyse)
    formatted_response = json.loads(response)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    max_value_key = max(emotions, key=emotions.get)
    max_value = max(emotions.values())
    return (max_value_key)