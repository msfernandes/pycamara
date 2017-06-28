from pycamara.base import BaseClient


class LegislativeBodyClient(BaseClient):

    def all(self):
        return self.safe(self._get('/orgaos'))

    def filter(self, **kwargs):
        return self.safe(self._get('/orgaos', **kwargs))

    def get(self, legislative_body_id):
        path = '/orgaos/{}'.format(legislative_body_id)
        return self.safe(self._get(path))

    def events(self, legislative_body_id):
        path = '/orgaos/{}/eventos'.format(legislative_body_id)
        return self.safe(self._get(path))
