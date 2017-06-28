from pycamara.base import BaseClient


class PropositionClient(BaseClient):

    def all(self):
        return self.safe(self._get('/proposicoes'))

    def filter(self, **kwargs):
        return self.safe(self._get('/proposicoes', **kwargs))

    def get(self, proposition_id):
        path = '/proposicoes/{}'.format(proposition_id)
        return self.safe(self._get(path))

    def proceedings(self, proposition_id):
        path = '/proposicoes/{}/tramitacoes'.format(proposition_id)
        return self.safe(self._get(path))

    def votings(self, proposal_id):
        path = '/proposicoes/{}/votacoes'.format(proposal_id)
        return self.safe(self._get(path))
