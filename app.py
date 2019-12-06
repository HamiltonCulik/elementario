from project import app

from flask import render_template

@app.route('/')
def index():
    return "<h1>Página principal do backend. Você não deveria estar aqui.</h1>"

app.run(debug=True)