import pandas as pd
import numpy as np
from datetime import datetime

class DataFetcher:
    @staticmethod
    def get_market_data(pair: str) -> pd.DataFrame:
        """
        Genera o obtiene un DataFrame con datos de precios recientes para el par indicado.
        Nota: Diseñado para simular o estructurar datos reales de velas de 5 minutos
        de manera limpia, segura y libre de bloqueos externos.
        """
        # Generar datos simulados estables basados en fluctuaciones reales para pruebas analíticas seguras
        np.random.seed(int(datetime.now().timestamp()) % 10000)
        
        periods = 100
        base_price = 100.0 if "INR" not in pair else 83.0
        
        # Simular una caminata aleatoria controlada con tendencia para el análisis técnico
        returns = np.random.normal(loc=0.0001, scale=0.0015, size=periods)
        price_series = base_price * np.cumprod(1 + returns)
        
        df = pd.DataFrame({
            'open': price_series * (1 + np.random.uniform(-0.0005, 0.0005, periods)),
            'high': price_series * (1 + np.random.uniform(0.0002, 0.0012, periods)),
            'low': price_series * (1 - np.random.uniform(0.0002, 0.0012, periods)),
            'close': price_series,
            'volume': np.random.randint(1000, 5000, size=periods)
        })
        
        return df

    @staticmethod
    def get_available_pairs() -> list:
        """Devuelve la lista de pares OTC configurados para analizar."""
        return [
            "USD/INR (OTC)",
            "EUR/USD (OTC)",
            "GBP/USD (OTC)",
            "USD/BRL (OTC)",
            "AUD/CAD (OTC)"
        ]
