from pycamara import exceptions
from pycamara.clients import cd
from pycamara.django_camara import models
from pycamara.django_camara.importers import base


class CongressmanInfoImporter(base.BaseDynamicDataImporter):

    field_relation = {
        "id": "id",
        "congressman": "id",
        "legal_name": "nomeCivil",
        "cpf": "cpf",
        "birthdate": "dataNascimento",
        "birth_state": "ufNascimento",
        "birth_city": "municipioNascimento",
        "deathdate": "dataFalecimento",
        "gender": "sexo",
        "site_url": "urlWebsite",
        "education": "escolaridade",
    }

    def get_model(self):
        return models.CongressmanInfo

    def clean_congressman(self, data):
        return models.Congressman.objects.get(id=data)

    def clean_birth_state(self, data):
        try:
            return models.State.objects.get(initials=data)
        except models.State.DoesNotExist:
            return None


class CongressmanImporter(base.BaseImporter):

    field_relation = {
        'id': 'id',
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

    def after_save_object(self, obj):
        try:
            data = cd.congressmen.get(obj.id)
            CongressmanInfoImporter(data).save_data()
        except exceptions.ClientError as e:
            error_json = e.response.json()
            if error_json['status'] != 404:
                raise e

    def clean_party(self, data):
        party_id = int(data.split('/')[-1])
        return models.Party.objects.get(id=party_id)

    def clean_state(self, data):
        return models.State.objects.get(initials=data)

    def clean_legislature(self, data):
        return models.Legislature.objects.get(id=data)
