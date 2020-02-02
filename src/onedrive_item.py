from onedrivesdk import ItemRequestBuilder
from onedrivesdk import options


class OnedriveItem:
    def __init__(self, onedriveIo, fileId, file=None):
        self.onedriveIo = onedriveIo
        self.fileId = fileId
        self.props = {}
        self._file = file
        self._ref = None

    def file(self):
        if self._file == None:
            self._file = self.onedriveIo.cache.item(self.ref())
        return self._file

    def ref(self):
        if self._ref == None:
            if self.fileId.startswith("/"):
                self._ref = self.onedriveIo.onedriveApi.client.item(
                    drive='me', path=self.fileId)
            else:
                self._ref = self.onedriveIo.onedriveApi.client.item(
                    drive='me', id=self.fileId)
        return self._ref

    def parent(self):
        fileId = self.file().parent_reference.id
        return OnedriveItem(self.onedriveIo, fileId)

    def children(self):
        return map(lambda ref: OnedriveItem(self.onedriveIo, ref[0], ref[1]), enumerate(self.onedriveIo.cache.item(self.ref().children)))

    def name(self):
        return self.file().name

    def isFolder(self):
        return self.file().folder != None

    def isFile(self):
        return not self.isFolder()

    def id(self):
        return self.file().id

    def size(self):
        return self.file().size

    def download_url(self):
        if '@content.downloadUrl' in self.file()._prop_dict:
            return self.file()._prop_dict['@content.downloadUrl']
        return None

    def read(self, offset, size):
        builder = ItemRequestBuilder(
            self.download_url(), self.onedriveIo.onedriveApi.client)
        rangeOption = options.HeaderOption(
            "Range", "bytes="+str(offset)+"-"+str(offset + size - 1))
        request = builder.request(options=[rangeOption])

        return request.download_item("/dev/null").content

    def tags(self):
        return self.ref().tags
        # return self.file.path
