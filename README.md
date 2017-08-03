# coincheck 

coincheck
The easiest Bitcoin Exchange in Japan
https://coincheck.jp/

## Install

```
pip install git+https://github.com/coincheckjp/coincheck-python
```

## Usage

```python
from coincheck.coincheck import CoinCheck
import logging

# CoinCheck.DEBUG = True
# CoinCheck.DEBUG_LEVEL = logging.DEBUG
coinCheck = CoinCheck('ACCESS_KEY', 'API_SECRET')

#Public API
res = coinCheck.ticker.all()
res = coinCheck.trade.all()
res = coinCheck.order_book.all()

# Private API
# 新規注文
# "buy" 指値注文 現物取引 買い
# "sell" 指値注文 現物取引 売り
# "market_buy" 成行注文 現物取引 買い
# "market_sell" 成行注文 現物取引 売り
# "leverage_buy" 指値注文 レバレッジ取引新規 買い
# "leverage_sell" 指値注文 レバレッジ取引新規 売り
# "close_long" 指値注文 レバレッジ取引決済 売り
# "close_short" 指値注文 レバレッジ取引決済 買い
params = {
    'rate': 2850,
    'amount': 0.00508771,
    'order_type': 'buy',
    'pair': 'btc_jpy'
}
res = coinCheck.order.create(params);

# 未決済の注文一覧
res = coinCheck.order.opens(params);
params = {
    'id': '2953613'
}
res = coinCheck.order.cancel(params);

# 取引履歴
res = coinCheck.order.transactions(params);

# ポジション一覧
res = coinCheck.leverage.positions(params);

# 残高
res = coinCheck.account.balance(params);

# レバレッジアカウントの残高
res = coinCheck.account.leverage_balance(params);

# アカウント情報
res = coinCheck.account.info(params);

# ビットコインの送金
params = {
    'address': '1Gp9MCp7FWqNgaUWdiUiRPjGqNVdqug2hY',
    'amount': '0.0002'
};
res = coinCheck.send.create(params);

# ビットコインの送金履歴
params = {
    'currency': "BTC"
};
res = coinCheck.send.all(params);

# ビットコインの受け取り履歴
params = {
    'currency': 'BTC'
};
res = coinCheck.deposit.all(params);

# ビットコインの高速入金
params = {
    'id': 2222
};
res = coinCheck.deposit.fast(params);

# 銀行口座一覧
res = coinCheck.bank_account.all(params);

# 銀行口座の登録
params = {
    'bank_name': "田中 田中",
    'branch_name': "田中 田中",
    'bank_account_type': "futsu",
    'number': "1234567",
    'name': "田中 田中"
};
res = coinCheck.bank_account.create(params);

# 銀行口座の削除
params = {
    'id': 2222
};
res = coinCheck.bank_account.delete(params);

# 出金履歴
res = coinCheck.withdraw.all(params);

# 出金申請の作成
params = {
    'bank_account_id': 2222,
    'amount': 50000,
    'currency': 'JPY',
    'is_fast': False
};
res = coinCheck.withdraw.create(params);

# 出金申請のキャンセル
params = {
    'id': 2222
};
res = coinCheck.withdraw.cancel(params);

# 借入申請
params = {
    'amount': '0.01',
    'currency': 'BTC'
};
res = coinCheck.borrow.create(params);

# 借入中一覧
res = coinCheck.borrow.matches(params);

# 返済
params = {
    'id': '1135'
};
res = coinCheck.borrow.repay(params);

# レバレッジアカウントへの振替
params = {
    'amount': 100,
    'currency': 'JPY'
};
res = coinCheck.transfer.to_leverage(params);

# レバレッジアカウントからの振替
params = {
    'amount': 100,
    'currency': 'JPY'
};
res = coinCheck.transfer.from_leverage(params);

print('\nThe result:')
print(res)
```

## License
MIT
