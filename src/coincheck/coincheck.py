import http.client
import time
import json
import hmac
import hashlib
import base64
import urllib
import logging
from coincheck.servicebase import ServiceBase

class CoinCheck:
    DEBUG = False
    DEBUG_LEVEL = logging.INFO
    apiBase = 'coincheck.jp'

    def __init__(self, accessKey, secretKey, options = {}):
        self.accessKey = accessKey
        self.secretKey = secretKey

        if (self.DEBUG):
            logging.basicConfig()
            self.logger = logging.getLogger('CoinCheck')
            self.logger.setLevel(self.DEBUG_LEVEL)
            self.requests_log = logging.getLogger("requests.packages.urllib3")
            self.requests_log.setLevel(self.DEBUG_LEVEL)
            self.requests_log.propagate = True
            http.client.HTTPSConnection.debuglevel = self.DEBUG_LEVEL

    def __getattr__(self, attr):
        attrs = ['ticker', 'trade', 'order_book', 'order', 'leverage', 'account'
                , 'send', 'deposit', 'bank_account', 'withdraw', 'borrow', 'transfer']

        if attr in attrs:
            #dynamic import module
            moduleName = attr.replace('_', '')
            module = __import__('coincheck.' + moduleName)
            #uppercase first letter
            className = attr.title().replace('_', '')
            module = getattr(module, moduleName)
            class_ = getattr(module, className)
            #dynamic create instance of class
            func = class_(self)
            setattr(self, attr, func)
            return func
        else:
            raise AttributeError('Unknown accessor ' + attr)

    def setSignature(self, path):
        nonce = str(round(time.time() * 1000000))
        url = 'https://' + self.apiBase + path
        message = nonce + url
        signature = hmac.new(self.secretKey.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()
        self.request_headers.update({
                'ACCESS-NONCE': nonce,
                'ACCESS-KEY': self.accessKey,
                'ACCESS-SIGNATURE': signature
            })

        if (self.DEBUG):
            self.logger.info('Set signature...')
            self.logger.debug('\n\tnone: %s\n\turl: %s\n\tmessage: %s\n\tsignature: %s', nonce, url, message, signature)

    def request(self, method, path, params):
        if (method == ServiceBase.METHOD_GET and len(params) > 0):
            path = path + '?' + urllib.parse.urlencode(params)
        data = ''
        self.request_headers = {}
        if (method == ServiceBase.METHOD_POST or method == ServiceBase.METHOD_DELETE):
            self.request_headers = {
                'content-type': "application/json"
            }
            path = path + '?' + urllib.parse.urlencode(params)
        self.setSignature(path)

        self.client = http.client.HTTPSConnection(self.apiBase)
        if (self.DEBUG):
            self.logger.info('Process request...')
        self.client.request(method, path, data, self.request_headers)
        res = self.client.getresponse()
        data = res.read()
        return data.decode("utf-8")