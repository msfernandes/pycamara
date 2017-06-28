from pycamara.base import BaseClient


class ReferenceClient(BaseClient):

    def congressman_status(self):
        return self.safe(self._get('/referencias/situacoesDeputado'))

    def event_status(self):
        return self.safe(self._get('/referencias/situacoesEvento'))

    def legislative_body_status(self):
        return self.safe(self._get('/referencias/situacoesOrgao'))

    def proposal_status(self):
        return self.safe(self._get('/referencias/situacoesProposicao'))

    def event_types(self):
        return self.safe(self._get('/referencias/tiposEvento'))

    def legislative_body_types(self):
        return self.safe(self._get('/referencias/tiposOrgao'))

    def proposal_types(self):
        return self.safe(self._get('/referencias/tiposProposicao'))

    def states(self):
        return self.safe(self._get('/referencias/uf'))
