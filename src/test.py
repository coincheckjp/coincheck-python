from coincheck.coincheck import CoinCheck
import logging

# CoinCheck.DEBUG = True
# CoinCheck.DEBUG_LEVEL = logging.DEBUG
coinCheck = CoinCheck('ACCESS_KEY', 'API_SECRET')

#Public API
res = coinCheck.ticker.all()
# res = coinCheck.trade.all()
# res = coinCheck.order_book.all()

#Private API
# params = {}
# params = {
#     'rate': 2850,
#     'amount': 0.00508771,
#     'order_type': 'buy',
#     'pair': 'btc_jpy'
# }
# res = coinCheck.order.create(params);
# res = coinCheck.order.opens(params);
# params = {
#     'id': '2953613'
# }
# res = coinCheck.order.cancel(params);
# res = coinCheck.order.transactions(params);

# res = coinCheck.leverage.positions();
# params = {'status': 'open'}
# res = coinCheck.leverage.positions(params);

# res = coinCheck.account.balance(params);
# res = coinCheck.account.leverage_balance(params);
# res = coinCheck.account.info(params);

# params = {
#     'address': '1Gp9MCp7FWqNgaUWdiUiRPjGqNVdqug2hY',
#     'amount': '0.0002'
# };
# res = coinCheck.send.create(params);
# params = {
#     'currency': "BTC"
# };
# res = coinCheck.send.all(params);

# params = {
#     'currency': 'BTC'
# };
# res = coinCheck.deposit.all(params);
# params = {
#     'id': 2222
# };
# res = coinCheck.deposit.fast(params);

# res = coinCheck.bank_account.all(params);
# params = {
#     'bank_name': "田中 田中",
#     'branch_name': "田中 田中",
#     'bank_account_type': "futsu",
#     'number': "1234567",
#     'name': "田中 田中"
# };
# res = coinCheck.bank_account.create(params);
# params = {
#     'id': 2222
# };
# res = coinCheck.bank_account.delete(params);

# res = coinCheck.withdraw.all(params);
# params = {
#     'bank_account_id': 2222,
#     'amount': 50000,
#     'currency': 'JPY',
#     'is_fast': False
# };
# res = coinCheck.withdraw.create(params);
# params = {
#     'id': 2222
# };
# res = coinCheck.withdraw.cancel(params);

# params = {
#     'amount': '0.01',
#     'currency': 'BTC'
# };
# res = coinCheck.borrow.create(params);
# res = coinCheck.borrow.matches(params);
# params = {
#     'id': '1135'
# };
# res = coinCheck.borrow.repay(params);

# params = {
#     'amount': 100,
#     'currency': 'JPY'
# };
# res = coinCheck.transfer.to_leverage(params);
# params = {
#     'amount': 100,
#     'currency': 'JPY'
# };
# res = coinCheck.transfer.from_leverage(params);

print('\nThe result:')
print(res)