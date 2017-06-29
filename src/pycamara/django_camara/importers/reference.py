from pycamara.django_camara import models
from pycamara.django_camara.importers.base import BaseImporter
from pycamara.clients import cd


class ReferenceImporter(BaseImporter):

    field_relation = {
        'initials': 'sigla',
        'name': 'nome',
        'description': 'descricao'
    }


class CongressmanStatusImporter(ReferenceImporter):

    def get_model(self):
        return models.CongressmanStatus

    def get_data(self):
        return cd.references.congressman_status()


class EventStatusImporter(ReferenceImporter):

    def get_model(self):
        return models.EventStatus

    def get_data(self):
        return cd.references.event_status()


class EventTypeImporter(ReferenceImporter):

    def get_model(self):
        return models.EventType

    def get_data(self):
        return cd.references.event_types()


class LegislativeBodyStatusImporter(ReferenceImporter):

    def get_model(self):
        return models.LegislativeBodyStatus

    def get_data(self):
        return cd.references.legislative_body_status()


class LegislativeBodyTypeImporter(ReferenceImporter):

    def get_model(self):
        return models.LegislativeBodyType

    def get_data(self):
        return cd.references.legislative_body_types()


class PropositionStatusImporter(ReferenceImporter):

    def get_model(self):
        return models.PropositionStatus

    def get_data(self):
        return cd.references.proposition_status()


class PropositionTypeImporter(ReferenceImporter):

    def get_model(self):
        return models.PropositionType

    def get_data(self):
        return cd.references.proposition_types()


class StatesImporter(ReferenceImporter):

    def get_model(self):
        return models.State

    def get_data(self):
        return cd.references.states()
