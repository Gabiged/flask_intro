from flask import Flask, render_template, request
'''Sukurti programą, kuri puslapyje localhost:5000/keliamieji parodytų 
visus keliamuosius metus nuo 1900 iki 2100 metų.'''


app = Flask(__name__)

@app.route("/")
def keliamieji():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)