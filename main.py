from django.shortcuts import redirect
from flask import Flask, render_template, request
import tina

app = Flask(__name__)
app.static_folder = 'static'

Tina = tina.Tina

chatbot = Tina()

@app.route("/")
async def index():
    return render_template("index.html")

@app.route("/get")
async def get_bot_response():
    userText = request.args.get('msg')
    return chatbot.block(message=userText)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)