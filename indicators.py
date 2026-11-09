import pandas as pd
import numpy as np

class TechnicalIndicators:
    @staticmethod
    def calculate_ema(series: pd.Series, period: int) -> pd.Series:
        """Calcula la Media Móvil Exponencial (EMA)."""
        return series.ewm(span=period, adjust=False).mean()

    @staticmethod
    def calculate_rsi(series: pd.Series, period: int = 14) -> pd.Series:
        """Calcula el Índice de Fuerza Relativa (RSI)."""
        delta = series.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    @staticmethod
    def calculate_bollinger_bands(series: pd.Series, period: int = 20, std_dev: float = 2.0):
        """Calcula las Bandas de Bollinger (Banda Media, Superior e Inferior)."""
        middle = series.rolling(window=period).mean()
        std = series.rolling(window=period).std()
        upper = middle + (std * std_dev)
        lower = middle - (std * std_dev)
        return upper, middle, lower

    @staticmethod
    def calculate_macd(series: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9):
        """Calcula el MACD y su línea de señal."""
        exp_fast = series.ewm(span=fast, adjust=False).mean()
        exp_slow = series.ewm(span=slow, adjust=False).mean()
        macd_line = exp_fast - exp_slow
        signal_line = macd_line.ewm(span=signal, adjust=False).mean()
        histogram = macd_line - signal_line
        return macd_line, signal_line, histogram
