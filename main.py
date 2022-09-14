from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Cia mano pirmas flask puslapis</h>"

if __name__ == "__main__":
    app.run(debug=True)