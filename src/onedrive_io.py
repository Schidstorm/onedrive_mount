from onedrive_item import OnedriveItem
from onedrive_cache import OnedriveCache


class OnedriveIO:
    def __init__(self, onedriveApi):
        self.onedriveApi = onedriveApi
        self.cache = OnedriveCache(self)

    def root(self):
        return OnedriveItem(self, 'root')

    def fromPath(self, path):
        return OnedriveItem(self, path)

    def exists(self, path):
        try:
            return self.cache.item(self.onedriveApi.client.item(
                drive='me', path=path)) != False
        except:
            return False
