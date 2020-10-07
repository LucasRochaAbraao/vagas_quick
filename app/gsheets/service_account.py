#!/usr/bin/env python3
"""
Esse repositorio consulta um formulário no google forms
e cria uma simples api com o resultado, para preencher
os campos de vagas abertas no site quick.com.br
                             } (
Author: Lucas Rocha Abraão  (   ) )
Date: 04/08/2020             ) { (
License: GNU GPLv3        ___|___)_
                       .-'---------|
                      ( C|/\/\/\/\/|
                       '-./\/\/\/\/|
                         '_________'
                          '-------'
"""
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import os

def auth(sheet):
    full_path_service_account = os.path.join(os.path.dirname(__file__), 'creds/service_account.json')
    creds = ServiceAccountCredentials.from_json_keyfile_name(full_path_service_account)
    client = gspread.authorize(creds)
    planilha = client.open(sheet).sheet1
    return planilha

def consultar_planilha(planilha):
    listaDeVagas = []
    for indice, _ in enumerate(planilha.col_values(1)):
        vaga_atual = []
        for ind, item in enumerate(planilha.row_values(indice+2)):
            if ind == 0: # pra vaga não ficar em formato de lista
                vaga_atual.append(item)
            else: # 
                vaga_atual.append(item.split('; '))
        listaDeVagas.append(dict(zip(['vaga', 'requisitos', 'atividades'], vaga_atual)))
    return listaDeVagas

if __name__ == '__main__':
    sheet = auth("VAGAS QUICK")
    vagas = consultar_planilha(sheet)
    del vagas[-1] # por algum motivo tem um dict vazio aqui, só limpando msm.

    for vaga in vagas:
        print(vaga)
