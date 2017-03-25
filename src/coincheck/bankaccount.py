from coincheck.servicebase import ServiceBase

class BankAccount(ServiceBase):
    baseUrl = '/api/bank_accounts'
    
    def create(self, params = {}):
        defaults = {
            'bank_name': "",
            'branch_name': "",
            'bank_account_type': "",
            'number': "",
            'name': ""
        }
        defaults.update(params)
        params = defaults.copy()
        return self.coinCheck.request(ServiceBase.METHOD_POST, self.baseUrl, params)

    def all(self, params = {}):
        return self.coinCheck.request(ServiceBase.METHOD_GET, self.baseUrl, params)

    def delete(self, params = {}):
        defaults = {
            'id': ""
        }
        defaults.update(params)
        params = defaults.copy()
        return self.coinCheck.request(ServiceBase.METHOD_DELETE, self.baseUrl + '/' + str(params['id']), params)