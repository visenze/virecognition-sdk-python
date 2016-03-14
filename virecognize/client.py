from requests.auth import HTTPBasicAuth
from .bind import bind_method


class ViRecognitionAPI(object):
    def __init__(self, access_key, secret_key):
        # self.host = "http://virecognition.visenze.com/"
        self.host = 'http://119.81.18.174:8082/'
        self.access_key = access_key
        self.secret_key = secret_key
        self.auth_info = HTTPBasicAuth(self.access_key, self.secret_key)

    def image_recognize(self, url, tag_group):
        path = 'image/recognize'
        method = 'POST'
        raw_parameters = {
            'url': url,
            'tag_group': tag_group
        }
        # parameters = build_parameters(path, raw_parameters)
        resp = bind_method(self, path, method, raw_parameters)
        return resp

    def video_recognize(self, url, tag_group):
        path = 'video/recognize_async'
        method = 'POST'
        raw_parameters = {
            'url': url,
            'tag_group': tag_group
        }
        # parameters = build_parameters(path, raw_parameters)
        resp = bind_method(self, path, method, raw_parameters)
        return resp

    def video_enquiry(self, transaction_id):
        path = 'video/enquiry'
        method = 'GET'
        raw_parameters = {
            'transaction_id': transaction_id
        }
        # parameters = build_parameters(path, raw_parameters)
        resp = bind_method(self, path, method, raw_parameters)

        return resp
