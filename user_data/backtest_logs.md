
## Date Range 1 mart 2021 - 4 mayıs 2021(2 ay) Market Change 284%

**parameters:**
```
  minimal_roi = {
      "0": 0.05
  }

  # Optimal stoploss designed for the strategy
  stoploss = -0.15

  # Optimal timeframe for the strategy
  timeframe = '15m'
```

**buy:**
```
(dataframe['rsi'] > 25) &
(dataframe['close'] < dataframe['bb_middleband'])
```

**sell:**
```
(dataframe['rsi'] > 70) &
(dataframe['close'] > dataframe['bb_upperband'])
```

**1. Total profit % : 98.94%**
**2. Total profit % : 113.81%** (stoploss=0.25)
**3. Total profit % : 122.29%** (std=3)
**4. without rsi < 25, Total profit % : 132.91%**

## Date Range 1 ocak 2020 - 6 mayıs 2021(2 ay) Market Change 3869%
**1. 394.66%**
**2. 416.81%**
**3. 425.68%**
**4. 456%**
**5. rsi > 75 453.12%**
**6. rsi > 80 453.06%**
**7. rsi<25 & roi disable 579%**



---- 1.1.2021 - 10.5.2021
timeframe 1m
trailing_stop = True

bbrsi-bendeki:217.2% (stoploss = -0.15)
bbrsi-sizdeki:68.49% % (stoploss = -0.20)
bncv5:92.86%


----- 1.1.2021 - 15.5.2021

**1**
buy:
(dataframe['rsi'] < 74)
         & (dataframe['close'] < dataframe['bb_middleband'])

sell:
(dataframe['close'] > dataframe['bb_upperband'])

profit: 149%

**2**
buy:
(dataframe['rsi'] < 74)
         & (dataframe['close'] < dataframe['bb_middleband'])
         & dataframe['ema20'] > dataframe['ema50']

sell: same as 1

profit: 104%

**3**
buy:
dataframe['ema20'] > dataframe['ema50']

sell:
(qtpylib.crossed_above(dataframe['ema50'], dataframe['ema20']))

profit:163%

**4**
buy:
 (qtpylib.crossed_above(dataframe['ema20'], dataframe['ema50']))

sell: same as 3

profit: 106%

**5**
buy:
(dataframe['close'] < dataframe['bb_middleband'])
       & dataframe['ema20'] > dataframe['ema50']
sell:
 same as 3

 profit:134%

 **6**
 buy: same as 5

sell:

(dataframe['close'] > dataframe['bb_upperband'])
        |
       (qtpylib.crossed_above(dataframe['ema50'], dataframe['ema20']))
       | (dataframe['rsi'] > 80)

profit: 104%
