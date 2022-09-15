from flask import Flask, render_template, request
'''Sukurti programą, kuri turėtų statinį puslapį, pvz. localhost:5000 su norimu tekstu 
(rekomenduojama naudoti šablonus)'''


app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Mano pirmasis puslapis</h1>"
if __name__ == "__main__":
    app.run(debug=True)

