from coincheck.servicebase import ServiceBase

class OrderBook(ServiceBase):
    baseUrl = '/api/order_books'
    
    def all(self, params = {}):
        return self.coinCheck.request(ServiceBase.METHOD_GET, self.baseUrl, params)