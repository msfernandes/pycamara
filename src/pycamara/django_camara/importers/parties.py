from pycamara.django_camara import models
from pycamara.django_camara.importers.base import BaseImporter
from pycamara.clients import cd


class PartyImporter(BaseImporter):

    field_relation = {
        'id': 'id',
        'name': 'nome',
        'initials': 'sigla',
    }

    def get_model(self):
        return models.Party

    def get_data(self):
        return cd.parties.all()
