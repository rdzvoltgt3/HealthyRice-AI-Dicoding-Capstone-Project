from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
from vercel.blob import BlobClient


@deconstructible
class VercelBlobStorage(Storage):
    def __init__(self):
        self._client = None  
    @property
    def client(self):
        if self._client is None:
            self._client = BlobClient()
        return self._client

    def _save(self, name, content):
        data = content.read()
        content_type = getattr(content, "content_type", None) or "application/octet-stream"
        uploaded = self.client.put(name, data, access="public", content_type=content_type)

        return uploaded.url

    def url(self, name):
        return name  

    def exists(self, name):

        return False

    def size(self, name):
        return self.client.head(name).size

    def delete(self, name):
        self.client.delete([name])

    def get_available_name(self, name, max_length=None):

        return name
