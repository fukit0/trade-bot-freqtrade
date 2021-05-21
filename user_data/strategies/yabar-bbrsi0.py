# --- Do not remove these libs ---
from freqtrade.strategy.interface import IStrategy
from typing import Dict, List
from functools import reduce
from pandas import DataFrame
from datetime import datetime
from freqtrade.persistence import Trade
from freqtrade.strategy import stoploss_from_open
# --------------------------------

import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib


class YABAR2(IStrategy):
    # 2
    # 3
    # 4
    # 5
    # 7
    minimal_roi = {
        "0": 0.1
    }

    stoploss = -0.99

    timeframe = '15m'

    order_types = {
        "buy": "limit",
        "sell": "limit",
        "emergencysell": "market",
        "forcebuy": "market",
        "forcesell": "market",
        "stoploss": "market",
        "stoploss_on_exchange": True,
        "stoploss_on_exchange_interval": 60,
        "stoploss_on_exchange_limit_ratio": 0.99,
    }

    # trailing_stop = True
    # trailing_stop_positive = 0.293
    # trailing_stop_positive_offset = 0.362
    # trailing_only_offset_is_reached = True


    use_custom_stoploss = True
    def custom_stoploss(self, pair: str, trade: 'Trade', current_time: datetime, current_rate: float, current_profit: float, **kwargs) -> float:
        if current_profit > 0.90:
            return stoploss_from_open(0.85, current_profit)
        elif current_profit > 0.80:
            return stoploss_from_open(0.72, current_profit)
        elif current_profit > 0.70:
            return stoploss_from_open(0.62, current_profit)
        elif current_profit > 0.60:
            return stoploss_from_open(0.52, current_profit)
        elif current_profit > 0.50:
            return stoploss_from_open(0.42, current_profit)
        elif current_profit > 0.40:
            return stoploss_from_open(0.32, current_profit)
        elif current_profit > 0.30:
            return stoploss_from_open(0.22, current_profit)
        elif current_profit > 0.20:
            return stoploss_from_open(0.12, current_profit)
        elif current_profit > 0.06:
            return stoploss_from_open(0.05, current_profit)
        return 1


    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # RSI
        dataframe['rsi'] = ta.RSI(dataframe, timeperiod=14)

        # Bollinger Bands
        bollinger = qtpylib.bollinger_bands(qtpylib.typical_price(dataframe), window=20, stds=2)
        dataframe['bb_lowerband'] = bollinger['lower']
        dataframe['bb_middleband'] = bollinger['mid']
        dataframe['bb_upperband'] = bollinger['upper']


        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                ((dataframe['rsi'] < 35)
                & (dataframe['close'] < dataframe['bb_lowerband']) )
            ),
            'buy'] = 1

        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                # (dataframe['rsi'] > 85)
                # &
                # (dataframe['close'] > dataframe['bb_upperband'])
            ),
            'sell'] = 1

        return dataframe
