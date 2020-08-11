from flask import jsonify
from app import app
from app.gsheets import service_account

@app.route('/', methods=['GET'])
def vagas():
    sheet = service_account.auth("VAGAS QUICK")
    vagas = service_account.consultar_planilha(sheet)
    del vagas[:-1]

    return jsonify(service_account.consultar_planilha(sheet))

