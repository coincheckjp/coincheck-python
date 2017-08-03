from coincheck.servicebase import ServiceBase

class Deposit(ServiceBase):
    baseUrl = '/api/deposit_money'
    
    def all(self, params = {}):
        defaults = {
            'currency': ""
        }
        defaults.update(params)
        params = defaults.copy()
        return self.coinCheck.request(ServiceBase.METHOD_GET, self.baseUrl, params)

    def fast(self, params = {}):
        defaults = {
            'id': ""
        }
        defaults.update(params)
        params = defaults.copy()
        return self.coinCheck.request(ServiceBase.METHOD_POST, self.baseUrl + '/' + str(params['id']) + '/fast', params)