import requests
import re
import json
from six.moves.urllib.parse import quote


re_path_template = re.compile('{\w+}')


class ViRecognitionClientError(Exception):
    def __init__(self, error_message, status_code=None):
        self.status_code = status_code
        self.error_message = error_message

    def __str__(self):
        if self.status_code:
            return "(%s) %s" % (self.status_code, self.error_message)
        else:
            return self.error_message


class ViRecognitionAPIError(Exception):

    def __init__(self, status_code, error_type, error_message, *args, **kwargs):
        self.status_code = status_code
        self.error_type = error_type
        self.error_message = error_message

    def __str__(self):
        return "(%s) %s-%s" % (self.status_code, self.error_type, self.error_message)


def build_path(path, parameters):
    for variable in re_path_template.findall(path):
        name = variable.strip('{}')

        try:
            value = quote(parameters[name])
        except KeyError:
            raise Exception('No parameter value found for path variable: %s' % name)
        del parameters[name]

        path = path.replace(variable, value)

    return path


def build_parameters(path, raw_parameters):
    param_s = ''
    if path == 'recognition':
        param_s = '&'.join(['{0}={1}'.format(attr_name, attr_val) for attr_name, attr_val in raw_parameters.iteritems()])

    return param_s


def bind_method(api, path, method, parameters=None, files=None):
    if method.upper() == 'POST':
        method_func = requests.post
    elif method.upper() == 'GET':
        method_func = requests.get

    resp = method_func(api.host + path, files=parameters, auth=api.auth_info, timeout=10*60)

    if resp.status_code != 200:
        raise ViRecognitionAPIError(resp.status_code, "{0} error".format(path), "{0} error".format(path))

    resp_data = resp.json()

    return resp_data
