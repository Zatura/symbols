# Symbols  
Cryptocurrency symbols catalog library  

 [![Release](https://img.shields.io/badge/release-v0.6.1--pre--alpha-orange.svg)](https://github.com/zatura/symbols)
[![Python](https://img.shields.io/badge/Python-3.6|3.7|3.8|3.9|3.10|3.11-blue.svg)](https://github.com/zatura/symbols)

  


Get the advantage of IDE hints for every symbol, don't worry about repeatedly consulting exchange/symbol-specific information.
You can have all information in itself as an accessible object.

Disclaimer: The symbols data is updated automatically and periodically, the data in this library can be subject 
of skewed/lagged information, all the data come from official apis from its respective exchange. 
Use it at your own risk.
## Supported exchanges
- [Binance](https://binance.com)
- [Bitfinex](https://bitfinex.com)
- [Bitmex](https://bitmex.com)
- [Coinbase](https://coinbase.com)
- [Mercado Bitcoin](https://mercadobitcoin.com.br)
- [Kraken](https://kraken.com)
- [Kucoin](https://kucoin.com)

## Quickstart

### Install
```bash
pip install git+https://github.com/zatura/symbols.git
```
### Iterating
```python
from symbols import bitfinex
for symbol in bitfinex:
    print(symbol.name)
    print(symbol.significant_digits)
    print(symbol.min_order_size)
```
```
> symbol.name='t1INCH:USD' symbol.has_margin=False symbol.min_order_size=2.0
> symbol.name='t1INCH:UST' symbol.has_margin=False symbol.min_order_size=2.0
> symbol.name='tAAVE:USD' symbol.has_margin=False symbol.min_order_size=0.02
```    
### Usage
```python
from symbols import bitfinex


symbol = bitfinex.BTCUSD  

print(symbol)
> "tBTCUSD"

print(symbol.name)
> "tBTCUSD"

print(symbol.significant_digits)
> 5

print(symbol.min_margin)
> 5.0

print(symbol.initial_margin)
> 10.0

print(symbol.min_order_size)
> 0.00006

print(symbol.max_order_size)
> 2000.0

print(symbol.has_margin)
> True

print(symbol.exchange)
> "bitfinex"

bitfinex.BTCUSD == 'tBTCUSD'
> True

str(symbol)
> "tBTCUSD"

repr(symbol)
> "tBTCUSD"

print(bitfinex.BTCUSD)
> "tBTCUSD"
```
