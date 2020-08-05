#!/usr/bin/env python3
from flask import Flask, jsonify, request
from google_api_serviceaccount import google_api_serviceaccount as API
import sys

app = Flask(__name__)

@app.route('/vagas', methods=['GET'])
def receber_vagas():
    sheet = API.auth("VAGAS QUICK")
    
    vagas_coletadas = API.consultar_planilha(sheet)
    del vagas_coletadas[-1] # por algum motivo tem um dict vazio aqui, só limpando msm.

    return jsonify(vagas_coletadas)

if __name__ == '__main__':
    app.run(debug=True)

