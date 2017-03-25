from coincheck.servicebase import ServiceBase

class Send(ServiceBase):
    baseUrl = '/api/send_money'

    def create(self, params = {}):
        defaults = {
            'address': "",
            'amount': ""
        }
        defaults.update(params)
        params = defaults.copy()
        return self.coinCheck.request(ServiceBase.METHOD_POST, self.baseUrl, params)
    
    def all(self, params = {}):
        defaults = {
            'currency': ''
        }
        defaults.update(params)
        params = defaults.copy()
        return self.coinCheck.request(ServiceBase.METHOD_GET, self.baseUrl, params)