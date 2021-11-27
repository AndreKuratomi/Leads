from flask import current_app, jsonify, request
from app.models.app_models import Lead


def create_lead():
    # creation_date e last_visit devem ser preenchidos no momento da criação do Lead.
    # E-mail e telefone único;
    # Telefone obrigatoriamente no formato (xx)xxxxx-xxxx.
    # Dica!
    # Confira como utilizar o Regex em Python, utilize o fullmatch para a comparação.

    # Corpo da requisição obrigatoriamente apenas com name, email e phone, sendo todos os campos do tipo string.
    ...


def get_leads():
    # listar todos os leads por ordem de visitas em ordem decrescente
    # tratar erro: nenhum dado encontrado
    pass


def update_lead(email):
    # atualizar apenas o valor de visits e last_visit
    # cada requisição no valor de visits deve ser acrescida em 1;
    # cada requisição no valor de last_visit deve ser atualizado para adata do request;
    # 40, bom saída que não mostra nada
    # TRATAR ERROS: nenhum dado encontrado, Corpo da requisição obrigatoriamente apenas com email, deve ser uma string;
    pass


def delete_lead(email):
    # TRATAR ERROS: nenhum dado encontrado, Corpo da requisição obrigatoriamente apenas com email, deve ser uma string;
    pass
