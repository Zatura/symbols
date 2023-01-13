# Symbols  
Cyptocurrency symbols catalog library  
  
[![Python](https://img.shields.io/badge/Python-3.10|3.11-green.svg)](https://github.com/zautra/symbols)  
  


Get the advantage of IDE hints for every symbol, don't worry about repeatedly consulting exchange/symbol-specific information.
You can have all information in itself as an accessible object.

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

str(symbol)
> "tBTCUSD"

repr(symbol)
> "tBTCUSD"

print(bitfinex.BTCUSD)
> "tBTCUSD"
```
