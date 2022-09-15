from flask import Flask, render_template, request
'''Sukurti programą, kuri įvedus norimą žodį adreso eilutėje (po / simbolio)
ir paspaudus ENTER, atspausdintų jį penkis kartus.'''


app = Flask(__name__)

@app.route("/<zodis>")
def kartoti(zodis):
    return f"{zodis}" * 5
if __name__ == "__main__":
    app.run(debug=True)