from pycamara.base import BaseClient


class EventClient(BaseClient):

    def all(self):
        return self.safe(self._get('/eventos'))

    def filter(self, **kwargs):
        return self.safe(self._get('/eventos', **kwargs))
