from flask import Flask, render_template
app = Flask(__name__)

filme = [
    {"titulo": "Sr e Sra Smith", "diretor": "Doug Liman"},
    {"titulo": "Sr e Sra Smith", "diretor": "Doug Liman"}
]

@app.route('/')
def Lfilmes():
    return render_template('Filmes.html', Lista=filme)

app.run()