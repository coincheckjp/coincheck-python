from coincheck.servicebase import ServiceBase

class Borrow(ServiceBase):
    baseUrl = '/api/lending/borrows'

    def create(self, params = {}):
        defaults = {
            'amount': "",
            'currency': ""
        }
        defaults.update(params)
        params = defaults.copy()
        return self.coinCheck.request(ServiceBase.METHOD_POST, self.baseUrl, params)

    def matches(self, params = {}):
        return self.coinCheck.request(ServiceBase.METHOD_GET, self.baseUrl + '/matches', params)

    def repay(self, params = {}):
        defaults = {
            'id': ""
        }
        defaults.update(params)
        params = defaults.copy()
        return self.coinCheck.request(ServiceBase.METHOD_POST, self.baseUrl + '/' + str(params['id']) + '/repay', params)