import json
import requests


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json= input_json, headers = header)
    
    if response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None

    if response.status_code == 200:    
        formatted_response = json.loads(response.text)   
        anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy =formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        dominant_emotion = max(formatted_response['emotionPredictions'][0]['emotion'], key=formatted_response['emotionPredictions'][0]['emotion'].get)
    

    emotions_dict = {
        'anger':anger,
        'disgust':disgust,
        'fear':fear,
        'joy':joy,
        'sadness':sadness,
        'dominant_emotion': dominant_emotion
    }

    return emotions_dict

