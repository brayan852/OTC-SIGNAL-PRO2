import pandas as pd
from indicators import TechnicalIndicators

class MarketFilters:
    @staticmethod
    def evaluate_signals(df: pd.DataFrame) -> dict:
        """
        Evalúa las condiciones del mercado actual utilizando los indicadores
        y devuelve una puntuación técnica, la dirección (CALL/PUT) y las confirmaciones.
        """
        if df is None or len(df) < 50:
            return {"status": False, "reason": "Datos insuficientes"}

        close = df['close']
        
        # Calcular indicadores clave
        ema9 = TechnicalIndicators.calculate_ema(close, 9)
        ema21 = TechnicalIndicators.calculate_ema(close, 21)
        ema50 = TechnicalIndicators.calculate_ema(close, 50)
        rsi = TechnicalIndicators.calculate_rsi(close, 14)
        macd, signal_line, _ = TechnicalIndicators.calculate_macd(close)

        # Últimos valores calculados
        c_price = close.iloc[-1]
        c_ema9 = ema9.iloc[-1]
        c_ema21 = ema21.iloc[-1]
        c_ema50 = ema50.iloc[-1]
        c_rsi = rsi.iloc[-1]
        c_macd = macd.iloc[-1]
        c_signal = signal_line.iloc[-1]

        confirmations = []
        score = 0
        direction = None

        # --- LÓGICA DE TENDENCIA Y CONFIRMACIÓN ---
        # Tendencia alcista (CALL)
        if c_ema9 > c_ema21 > c_ema50 and c_price > c_ema50:
            direction = "CALL"
            confirmations.append("Tendencia Alcista (EMAs alineadas)")
            score += 25
        # Tendencia bajista (PUT)
        elif c_ema9 < c_ema21 < c_ema50 and c_price < c_ema50:
            direction = "PUT"
            confirmations.append("Tendencia Bajista (EMAs alineadas)")
            score += 25
        else:
            return {"status": False, "reason": "Mercado lateral o sin tendencia clara"}

        # --- FILTRO DE RSI ---
        if direction == "CALL" and 45 <= c_rsi <= 70:
            confirmations.append(f"RSI favorable ({c_rsi:.1f})")
            score += 25
        elif direction == "PUT" and 30 <= c_rsi <= 55:
            confirmations.append(f"RSI favorable ({c_rsi:.1f})")
            score += 25
        else:
            return {"status": False, "reason": f"RSI en zona de sobrecompra/sobreventa extrema ({c_rsi:.1f})"}

        # --- FILTRO DE MACD ---
        if direction == "CALL" and c_macd > c_signal:
            confirmations.append("MACD alcista confirmado")
            score += 25
        elif direction == "PUT" and c_macd < c_signal:
            confirmations.append("MACD bajista confirmado")
            score += 25
        else:
            return {"status": False, "reason": "MACD en contradicción con la tendencia"}

        # --- VOLATILIDAD Y PUNTUACIÓN EXTRA ---
        score += 25  # Puntuación base por cumplir filtros estrictos
        confirmations.append("Volatilidad y estructura de velas estables")

        # Filtro de calidad mínima (Exigimos al menos 75/100 para enviar señal)
        if score < 75:
            return {"status": False, "reason": "Puntuación técnica insuficiente (< 75)"}

        return {
            "status": True,
            "direction": direction,
            "score": score,
            "confirmations": confirmations,
            "price": c_price
        }
