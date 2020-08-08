from flask import Flask, jsonify
from google_api_serviceaccount import google_api_serviceaccount as google_api

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    sheet = google_api.auth("VAGAS QUICK")
    
    vagas_coletadas = google_api.consultar_planilha(sheet)
    del vagas_coletadas[-1] # por algum motivo tem um dict vazio aqui, só limpando msm.

    return jsonify(vagas_coletadas)

if __name__ == '__main__':
    app.run(debug=True)
