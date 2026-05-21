from flask import Flask, render_template # type: ignore

app = Flask(__name__)

@app.route("/")
def home():

    alunos = [
        {"nome": "Ana"},
        {"nome": "Carlos"},
        {"nome": "Maria"}
    ]

    usuario = {
        "nome": "Ana",
        "email": "ana@email.com"
    }

    return render_template(
        "index.html",
        nome="João",
        idade=25,
        nota=8,
        usuario=usuario,
        alunos=alunos
    )

if __name__ == "__main__":
    app.run(debug=True)