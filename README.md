# Vagas Quick
> Esse repositório contém o projeto que gerencia a API que o site da Quick consulta para divulgar vagas na página /trabalhe-conosco.
> São 2 projetos em 1, pois tem a API que o site da Quick consulta, que expõe as vagas. E também há um frontend desenvolvido para nosso RH gerenciar as vagas do banco de dados.

[![python-image]][python-url]
[![django-image]][django-url]
[![sqlite-image]][sqlite-url]

Nesse repositório você encontra informações de instalação, além de ter acesso ao código fonte, que inclui uma licença open source pra copiar 
(desde que use a mesma licença no seu projeto).


## Setup & Instalação
Primeiro é necessário instalar, configurar e ativar um ambiente virtual, para um melhor gerenciamento do projeto.
```
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
```

>Clone o repo
```
git clone https://github.com/LucasRochaAbraao/vagas_quick.git .
pip install -r requirements.txt
```

>crie um arquivo ".env" no diretório raiz:
```
SECRET_KEY='dasoijdoiasjdiojqwiodqwuidihdiuqw(gerado pelo django)'
```

## utilização
Utilize o seguinte comando para rodar o servidor na porta 9000, ou configure um servidor nginx.
- gunicorn vagas_project.asgi:application -k uvicorn.workers.UvicornWorker --forwarded-allow-ips='*' -b :9000


[python-image]: https://img.shields.io/static/v1?label=python&message=3.7&color=blue
[python-url]: https://www.python.org/downloads/release/python-370/

[django-image]: https://img.shields.io/static/v1?label=django&message=0.63+&color=blue
[django-url]: https://docs.djangoproject.com/en/3.1/

[sqlite-image]: https://img.shields.io/static/v1?label=sqlite&message=3&color=success
[sqlite-url]: https://docs.python.org/3/library/sqlite3.html

Distribuído sob a licença `GNU GENERAL PUBLIC LICENSE`. Veja `LICENSE` para mais informações.