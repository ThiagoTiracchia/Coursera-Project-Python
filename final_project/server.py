"""Module for the function."""
import json
from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask("emotionDetector")


@app.route("/emotionDetector", methods=['GET', 'POST'])
def emotion_analyzer():
    """Module for emotion analyzer."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response is None:
        return "Invalid text ! Please try again."
    formatted_response = json.loads(response)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    max_value_key = max(emotions, key=emotions.get)
    str1 = "The given text has been identified as "
    str2 = str(emotions)
    str3 = " the dominant emotion is "
    str4 = str(max_value_key)
    str5 = str1 + str2 + str3 + str4
    return str5


@app.route("/")
def render_index_page():
    """Module for index."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    