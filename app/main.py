from flask import Flask, jsonify
from google_api_serviceaccount import google_api_serviceaccount as API

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def receber_vagas():
        sheet = API.auth("VAGAS QUICK")
        
        vagas_coletadas = API.consultar_planilha(sheet)
        del vagas_coletadas[-1] # por algum motivo tem um dict vazio aqui, só limpando msm.

        return jsonify(vagas_coletadas)

    return app


