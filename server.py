from flask import Flask, render_template, request
from EmotionAnalysis.emotion_detection import emotion_detector
app = Flask("Sentiment Analyzer")
@app.route("/sentimentAnalyzer")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response =emotion_detector(text_to_analyze)
    label = response['label']
    score = response['score']
    return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)
@app.route("/")
def render_index_page():
    return render_template('index.html')
if __name__ == "__main__":
    app.run()   
