# symbols
Cyptocurrency symbols catalog library

## Why it's useful?  
You get the advantage of IDE hints, also, you don't need to worry about consulting exchange/symbol-specific information for every symbol.
By having all information in itself as an accessible object, you can integrate it on your project.

## Usage  

```python
from symbols import bitfinex

symbol = bitfinex.BTCUSD  


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

```