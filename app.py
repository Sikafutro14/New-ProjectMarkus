from flask import Flask
import os
port = int(os.environ.get("Port"))

app = Flask(__name__)



@app.route("/")
def home():
    return " just created my own web page "


if __name__ == "__main__":
    app.run(debug=True)    