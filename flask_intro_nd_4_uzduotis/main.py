from flask import Flask, render_template, request
'''Sukurti programą, kuri leistų įvesti metus ir paspaudus 
patvirtinimo mygtuką parodytų, ar jie yra keliamieji.'''


app = Flask(__name__)

@app.route("/")
def keliamieji():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)