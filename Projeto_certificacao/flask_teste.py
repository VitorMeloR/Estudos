from flask import Flask, jsonify
nome = input('sistema')
nome_dct = {'sistemas': nome}
app = Flask(__name__)

@app.route('/')
def homepage():
    jsonify(nome_dct)


app.run()