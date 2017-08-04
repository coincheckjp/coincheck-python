from coincheck.servicebase import ServiceBase

class Ticker(ServiceBase):
    baseUrl = '/api/ticker'
    
    def all(self, params = {}):
        return self.coinCheck.request(ServiceBase.METHOD_GET, self.baseUrl, params)