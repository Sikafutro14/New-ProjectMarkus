from flask import Flask
import os
Port = int(os.environ.get("PORT", 5000))

app = Flask(__name__)



@app.route("/")
def home():
    return " just created my own web page "


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=Port)    