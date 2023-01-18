# Symbols  
Cryptocurrency symbols catalog library  

 [![Release](https://img.shields.io/badge/release-v0.1.0--pre--alpha-orange.svg)](https://github.com/zautra/symbols)
[![Python](https://img.shields.io/badge/Python-3.10|3.11-blue.svg)](https://github.com/zautra/symbols)

  


Get the advantage of IDE hints for every symbol, don't worry about repeatedly consulting exchange/symbol-specific information.
You can have all information in itself as an accessible object.

Disclaimer: The symbols data is updated automatically and periodically, the data in this library can be subject 
of skewed/lagged information, all the data come from official apis from its respective exchange. 
Use it at your own risk.

## Quickstart

### Install
```bash
pip install git+https://github.com/zatura/symbols.git
```
  
### Usage
```python
from symbols import bitfinex

symbol = bitfinex.BTCUSD  

print(symbol)
> "tBTCUSD"

print(symbol.name)
> "tBTCUSD"

print(symbol.precision)
> 5

print(symbol.minimum_margin)
> 5.0

print(symbol.initial_margin)
> 10.0

print(symbol.minimum_order_size)
> 0.00006

print(symbol.maximum_order_size)
> 2000.0

print(symbol.margin)
> True

bitfinex.BTCUSD == 'tBTCUSD'
> True

str(symbol)
> "tBTCUSD"

repr(symbol)
> "tBTCUSD"

print(bitfinex.BTCUSD)
> "tBTCUSD"
```
