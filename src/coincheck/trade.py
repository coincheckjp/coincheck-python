from coincheck.servicebase import ServiceBase

class Trade(ServiceBase):
    baseUrl = '/api/trades'
    
    def all(self, params = {}):
        return self.coinCheck.request(ServiceBase.METHOD_GET, self.baseUrl, params)