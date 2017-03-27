from coincheck.servicebase import ServiceBase

class Account(ServiceBase):
    baseUrl = '/api/accounts'

    def balance(self, params = {}):
        return self.coinCheck.request(ServiceBase.METHOD_GET, self.baseUrl + '/balance', params)

    def leverage_balance(self, params = {}):
        return self.coinCheck.request(ServiceBase.METHOD_GET, self.baseUrl + '/leverage_balance', params)

    def info(self, params = {}):
        return self.coinCheck.request(ServiceBase.METHOD_GET, self.baseUrl, params)