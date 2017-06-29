from pycamara.django_camara import models
from pycamara.django_camara.importers.base import BaseImporter
from pycamara.clients import cd


class LegislatureImporter(BaseImporter):

    field_relation = {
        'start_date': 'dataInicio',
        'end_date': 'dataFim',
    }

    def get_model(self):
        return models.Legislature

    def get_data(self):
        return cd.legislatures.all()
