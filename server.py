"""
Flask server for emotion detection.

This module exposes endpoints to analyze text and return detected emotions.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze the input text and return detected emotions.

    Query Params:
        textToAnalyze (str): Text to analyze.

    Returns:
        str: Formatted string with emotion scores and dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! please try again!"

    return (
        "For the given statement, the system response is "
        f'"anger": {anger}, "disgust": {disgust}, "fear": {fear}, '
        f'"joy": {joy}, and "sadness": {sadness}. '
        f"The dominant emotion is {dominant_emotion}."
    )
@app.route("/")
def render_index_page():
    """
    Render the index page.

    Returns:
        HTML: index.html template.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    