start_candles, new_candle_cost = [int(x) for x in input().strip().split()]

candles = start_candles
burnt_candles = 0
hours = 0
while (candles > 0):
  hours += candles
  burnt_candles += candles
  extra_candles = burnt_candles % new_candle_cost 
  candles = burnt_candles // new_candle_cost
  burnt_candles = extra_candles

print(hours)