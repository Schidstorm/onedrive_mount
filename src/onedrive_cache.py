

class OnedriveCache:
    def __init__(self, onedriveIo):
        self._data = {}
        self.onedriveIo = onedriveIo

    def item(self, builder):
        if not builder._request_url in self._data:
            try:
                self._data[builder._request_url] = builder.get()
            except:
                self._data[builder._request_url] = False
        return self._data[builder._request_url]
