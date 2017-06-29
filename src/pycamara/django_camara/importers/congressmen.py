from pycamara.django_camara import models
from pycamara.django_camara.importers.base import BaseImporter
from pycamara.clients import cd


class CongressmanImporter(BaseImporter):

    field_relation = {
        'id': 'sigla',
        'name': 'nome',
        'photo_url': 'urlFoto',
        'party': 'uriPartido',
        'state': 'siglaUf',
        'legislature': 'idLegislatura'
    }

    def get_model(self):
        return models.Congressman

    def get_data(self):
        return cd.congressmen.all()

    def clean_party(self, data):
        party_id = int(data.split('/')[-1])
        return models.Party.objects.get(id=party_id)

    def clean_state(self, data):
        return models.State.objects.get(initials=data)

    def clean_legislature(self, data):
        return models.Legislature.objects.get(id=data)
