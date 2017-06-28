from pycamara.base import BaseClient


class LegislatureClient(BaseClient):

    def all(self):
        return self.safe(self._get('/legislaturas'))

    def get(self, legislature_id):
        path = '/legislaturas/{}'.format(legislature_id)
        return self.safe(self._get(path))

    def board_members(self, legislature_id):
        path = '/legislaturas/{}/mesa'.format(legislature_id)
        return self.safe(self._get(path))
