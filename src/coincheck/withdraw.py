from coincheck.servicebase import ServiceBase

class Withdraw(ServiceBase):
    baseUrl = '/api/withdraws'

    def create(self, params = {}):
        return self.coinCheck.request(ServiceBase.METHOD_POST, self.baseUrl, params)
    
    def all(self, params = {}):
        return self.coinCheck.request(ServiceBase.METHOD_GET, self.baseUrl, params)

    def cancel(self, params = {}):
        defaults = {
            'id': ""
        }
        defaults.update(params)
        params = defaults.copy()
        return self.coinCheck.request(ServiceBase.METHOD_DELETE, self.baseUrl + '/' + str(params['id']), params)