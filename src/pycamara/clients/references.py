from pycamara.base import BaseClient


class ReferenceClient(BaseClient):

    def congressman_status(self):
        return self.safe(self._get('/referencias/situacoesDeputado'))

    def event_status(self):
        return self.safe(self._get('/referencias/situacoesEvento'))

    def event_types(self):
        return self.safe(self._get('/referencias/tiposEvento'))

    def legislative_body_status(self):
        return self.safe(self._get('/referencias/situacoesOrgao'))

    def legislative_body_types(self):
        return self.safe(self._get('/referencias/tiposOrgao'))

    def proposition_status(self):
        return self.safe(self._get('/referencias/situacoesProposicao'))

    def proposition_types(self):
        return self.safe(self._get('/referencias/tiposProposicao'))

    def states(self):
        return self.safe(self._get('/referencias/uf'))
