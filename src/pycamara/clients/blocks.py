from pycamara.base import BaseClient


class BlockClient(BaseClient):

    def all(self):
        return self.safe(self._get('/blocos'))

    def filter(self, **kwargs):
        return self.safe(self._get('/blocos', **kwargs))

    def get(self, block_id):
        path = '/blocos/{}'.format(block_id)
        return self.safe(self._get(path))
