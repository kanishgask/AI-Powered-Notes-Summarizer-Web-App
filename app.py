from flask import Flask, render_template, request
from summarizer import summarize_text
from utils import clean_text

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    text = request.form["text"]
    
    if len(text.strip()) == 0:
        return render_template("index.html", summary="Please enter valid text!")

    cleaned = clean_text(text)
    summary = summarize_text(cleaned)

    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
