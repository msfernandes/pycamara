from pycamara.django_camara import models
from pycamara.django_camara.importers.base import BaseImporter
from pycamara.clients import cd


class LegislativeBodyImporter(BaseImporter):

    field_relation = {
        'initials': 'sigla',
        'name': 'nome',
        'legislative_body_type': 'idTipoOrgao'
    }

    def get_model(self):
        return models.LegislativeBody

    def get_data(self):
        return cd.legislative_bodies.all()

    def clean_legislative_body_type(self, data):
        return models.LegislativeBodyType.objects.get(id=data)
