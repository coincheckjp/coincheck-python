class ServiceBase:
    METHOD_GET = 'GET'
    METHOD_POST = 'POST'
    METHOD_DELETE = 'DELETE'

    def __init__(self, coinCheck):
        self.coinCheck = coinCheck
        if (coinCheck.DEBUG):
            self.logger = coinCheck.logger