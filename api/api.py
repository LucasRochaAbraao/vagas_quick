from flask import request, jsonify, Flask
from gsheets import service_account

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    sheet = service_account.auth("VAGAS QUICK")
    return jsonify(service_account.consultar_planilha(sheet))

app.run()