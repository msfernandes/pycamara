from pycamara.base import BaseClient


class VotingClient(BaseClient):

    def get(self, voting_id):
        path = '/votacoes/{}'.format(voting_id)
        return self.safe(self._get(path))

    def get_votes(self, voting_id):
        path = '/votacoes/{}/votos'.format(voting_id)
        return self.safe(self._get(path))
