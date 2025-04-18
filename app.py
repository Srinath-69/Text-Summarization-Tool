from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Initialize the summarization model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    if request.method == "POST":
        text = request.form["text"]
        if text:
            summary = summarizer(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
