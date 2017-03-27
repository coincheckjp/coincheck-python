from coincheck.servicebase import ServiceBase

class Transfer(ServiceBase):
    baseUrl = '/api/exchange/transfers'

    def to_leverage(self, params = {}):
        defaults = {
            'amount': "",
            'currency': ""
        }
        defaults.update(params)
        params = defaults.copy()
        return self.coinCheck.request(ServiceBase.METHOD_POST, self.baseUrl + '/to_leverage', params)

    def from_leverage(self, params = {}):
        defaults = {
            'amount': "",
            'currency': ""
        }
        defaults.update(params)
        params = defaults.copy()
        return self.coinCheck.request(ServiceBase.METHOD_POST, self.baseUrl + '/from_leverage', params)