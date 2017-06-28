from pycamara.base import BaseClient


class CongressmanClient(BaseClient):

    def all(self):
        return self.safe(self.get('/deputados'))

    def filter(self, **kwargs):
        return self.safe(self.get('/deputados', **kwargs))

    def expenses(self, deputy_id, **kwargs):
        path = '/deputados/{}/despesas'.format(deputy_id)
        return self.safe(self.get(path), **kwargs)

    def events(self, deputy_id, **kwargs):
        path = '/deputados/{}/eventos'.format(deputy_id)
        return self.safe(self.get(path), **kwargs)

    def legislative_bodies(self, deputy_id, **kwargs):
        path = '/deputados/{}/orgaos'.format(deputy_id)
        return self.safe(self.get(path), **kwargs)

    def status(self):
        path = '/referencias/situacoesDeputado'
        return self.safe(self.get(path))
