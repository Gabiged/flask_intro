from flask import Flask, render_template, request

# app = Flask(__name__)
#
# @app.route("/<vardas>")
# def home(vardas):
#     return f"Labas, {vardas}"
#
# if __name__ == "__main__":
#     app.run(debug=True)

# ats http://127.0.0.1:5000/Gabija, vietoje vardo belen kas gali buti

# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return render_template('index.html')
#
# if __name__ == "__main__":
#     app.run(debug=True)

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Skaiciavimai</title>
# </head>
# <body>
# <h>Skaiciavimai</h>
# {%for x in range (10)%}
# {%if x % 2 == 0%}
# <p>{{x}}</p>
# {%endif%}
# {%endfor%}
# </body>
# </html>

# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     vardai = ['Jonas Katalis', 'Linas Oksalis', 'Alma Puriene']
#     return render_template('index.html', sarasas=vardai)
#
# if __name__ == "__main__":
#     app.run(debug=True)

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        vardas = request.form["vardas"]
        return render_template("greetings.html", vardas=vardas)
    else:
        return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)


    # ats: http://127.0.0.1:5000/login