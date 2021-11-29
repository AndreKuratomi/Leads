from datetime import datetime
from flask import current_app, jsonify, request
from sqlalchemy import asc, desc
from app.models.app_models import Lead

import re

from exceptions.app_exceptions import AbsentError, InvalidPhoneError, NotFoundError, NotStringError
from sqlalchemy.exc import IntegrityError, ProgrammingError
from psycopg2.errors import UniqueViolation

from ipdb import set_trace

valid_keys = ["name", "email", "phone"]
check_keys = []
regex = "\(\w{2}\)\w{4}-\w{4}"


def create_lead():
    try:
        raw_data = request.get_json()

        data = {key: raw_data[key] for key in raw_data if key in valid_keys}

        new_lead = Lead(**data)

        keys = data.keys()
        for elems in keys:
            for sub_elems in valid_keys:
                if elems == sub_elems:
                    check_keys.append(elems)
        if len(check_keys) < 3:
            raise AbsentError

        values = data.values()
        for elems in values:
            if type(elems) != str:
                raise NotStringError

        phone = new_lead.phone
        if not re.search(regex, phone):
            raise InvalidPhoneError

        current_app.db.session.add(new_lead)
        current_app.db.session.commit()

        return jsonify(new_lead), 201

    except IntegrityError:
        # por que agora o debaixo não funciona mais?
        # if ie.orig.pgcode == UniqueViolation:
        return {"Error": "O email ou telefone já existentes no banco de dados!"}, 409

    except InvalidPhoneError as ipe:
        return ipe.message, 400

    except NotStringError as nse:
        return nse.message, 400

    except AbsentError as ae:
        return ae.message, 400


def get_leads():
    try:
        query = Lead.query.order_by(Lead.visits.desc()).all()

        if len(query) == 0:
            raise NotFoundError

        return jsonify(query), 200

    except NotFoundError as nfe:
        return nfe.message, 404

    except ProgrammingError:
        return {"Error": "nenhum dado encontrado"}, 404


def update_lead():
    try:
        to_update = request.get_json()

        values = to_update.values()
        for elems in values:
            if type(elems) != str:
                raise NotStringError

        all_leads = Lead.query.all()
        for elem in all_leads:
            if elem.email == to_update['email']:

                updating_last = datetime.now()
                new_visit = elem.visits + 1

                setattr(elem, 'last_visit', updating_last)
                setattr(elem,  'visits', new_visit)

                current_app.db.session.add(elem)
                current_app.db.session.commit()

                return "", 204
        else:
            raise NotFoundError

    except NotStringError as nse:
        return nse.message, 400

    except NotFoundError as nfe:
        return nfe.message, 404


def delete_lead():
    try:
        to_filter = request.get_json()

        values = to_filter.values()
        for elems in values:
            if type(elems) != str:
                raise NotStringError

        all_leads = Lead.query.all()
        for elem in all_leads:
            if elem.email == to_filter['email']:
                current_app.db.session.delete(elem)
                current_app.db.session.commit()
                return "", 204
        else:
            raise NotFoundError

    except NotStringError as nse:
        return nse.message, 400

    except NotFoundError as nfe:
        return nfe.message, 404
