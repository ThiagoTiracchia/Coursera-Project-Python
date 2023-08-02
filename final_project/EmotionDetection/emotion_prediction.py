from emotion_detection import emotion_detector 

def emotion_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    formatted_response = json.loads(response)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    max_value_key = max(emotions, key=emotions.get)
    return "The given statement, the system response is ", emotions, "The dominant emotion is" , max_value_key 


