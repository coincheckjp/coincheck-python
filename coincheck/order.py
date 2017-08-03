from coincheck.servicebase import ServiceBase

class Order(ServiceBase):
    baseUrl = '/api/exchange/orders'

    def create(self, params = {}):
        return self.coinCheck.request(ServiceBase.METHOD_POST, self.baseUrl, params)

    def cancel(self, params = {}):
        defaults = {
            'id': ""
        }
        defaults.update(params)
        params = defaults.copy()
        return self.coinCheck.request(ServiceBase.METHOD_DELETE, self.baseUrl + '/' + str(params['id']), params)
    
    def opens(self, params = {}):
        return self.coinCheck.request(ServiceBase.METHOD_GET, self.baseUrl + '/opens', params)
    
    def transactions(self, params = {}):
        return self.coinCheck.request(ServiceBase.METHOD_GET, self.baseUrl + '/transactions', params)