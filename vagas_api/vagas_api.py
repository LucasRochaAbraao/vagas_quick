from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from google_api_serviceaccount import google_api_serviceaccount as google_api

app = Flask(__name__)
api = Api(app)

class VagasQuick(Resource):
    def get(self):
        sheet = google_api.auth("VAGAS QUICK")
        vagas_coletadas = google_api.consultar_planilha(sheet)
        del vagas_coletadas[-1] # por algum motivo tem um dict vazio aqui, só limpando msm.

        return vagas_coletadas
        #return jsonify(vagas_coletadas)

api.add_resource(VagasQuick, '/')

if __name__ == '__main__':
    app.run(debug=True)