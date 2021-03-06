import netifaces
from bottle import response
from bottle import request


# Credits https://stackoverflow.com/a/11736402
def get_iface_ip():
    """
    Return the FIRST interface (other than lo) hat has an IP
    """
    interfaces = netifaces.interfaces()
    for i in interfaces:
        if i == 'lo':
            continue
        iface = netifaces.ifaddresses(i).get(netifaces.AF_INET)
        if iface is not None:
            for j in iface:
                return j['addr']


# Credits: https://stackoverflow.com/a/17262900
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors
