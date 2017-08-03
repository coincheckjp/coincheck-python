from coincheck.servicebase import ServiceBase

class Leverage(ServiceBase):
    baseUrl = '/api/exchange/leverage'
    
    def positions(self, params = {}):
        return self.coinCheck.request(ServiceBase.METHOD_GET, self.baseUrl + '/positions', params)