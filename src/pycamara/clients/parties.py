from pycamara.base import BaseClient


class PartyClient(BaseClient):

    def all(self):
        return self.safe(self._get('/partidos'))

    def filter(self, **kwargs):
        return self.safe(self._get('/partidos', **kwargs))

    def get(self, party_id):
        path = '/partidos/{}'.format(party_id)
        return self.safe(self._get(path))
