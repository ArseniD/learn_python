import socket


class Resolver:

    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        '''This special dunder-call method
           can be used to define classes, which when instantiated
           can be called using regular function call syntax'''

        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache
