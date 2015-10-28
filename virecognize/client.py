from requests.auth import HTTPBasicAuth
from .bind import bind_method, build_parameters


class ViRecognitionAPI(object):
    def __init__(self, access_key, secret_key):
        self.host = "http://virecognition.visenze.com/"
        self.access_key = access_key
        self.secret_key = secret_key
        self.auth_info = HTTPBasicAuth(self.access_key, self.secret_key)

    def recognition(self, url, tag_group):
        path = 'image/recognize'
        method = 'POST'
        raw_parameters = {
            'url': url,
            'tag_group': tag_group
        }
        # parameters = build_parameters(path, raw_parameters)
        resp = bind_method(self, path, method, raw_parameters)
        return resp
