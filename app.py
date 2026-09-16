from flask import Flask

app = Flask(__name__)





@app.route("/")
def func():
    return "Endi Abu yam serverda bolajonla"


if __name__ == "__main__":
    app.run()