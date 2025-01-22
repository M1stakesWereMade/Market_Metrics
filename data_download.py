import yfinance as yf
import pandas as pd


def fetch_stock_data(ticker, period='1mo'):
    """
    Загружает исторические данные о ценах акции с использованием yfinance.
    
    Args:
        ticker (str): Биржевой тикер компании (например, "AAPL").
        period (str): Период данных (например, "1mo", "6mo", "1y").
    
    Returns:
        pandas.DataFrame: Данные с колонками, включающими "Open", "High", "Low", "Close", "Volume".
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    """
    Добавляет скользящую среднюю (Moving Average) к данным.
    
    Args:
        data (pandas.DataFrame): Данные с колонкой "Close".
        window_size (int): Период скользящей средней.
    
    Returns:
        pandas.DataFrame: Данные с добавленной колонкой "Moving_Average".
    """
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_rsi(data, window=14):
    """
    Рассчитывает индекс относительной силы (RSI).
    
    Args:
        data (pandas.DataFrame): Данные с колонкой "Close".
        window (int): Период для расчета RSI.
    
    Returns:
        pandas.DataFrame: Данные с добавленной колонкой "RSI".
    """
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()

    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    return data


def calculate_macd(data, fast_period=12, slow_period=26, signal_period=9):
    """
    Рассчитывает индикатор MACD и сигнальную линию.
    
    Args:
        data (pandas.DataFrame): Данные с колонкой "Close".
        fast_period (int): Период для быстрой EMA.
        slow_period (int): Период для медленной EMA.
        signal_period (int): Период сигнальной линии.
    
    Returns:
        pandas.DataFrame: Данные с добавленными колонками "MACD_Line" и "Signal_Line".
    """
    data['MACD_Line'] = data['Close'].ewm(span=fast_period, adjust=False).mean() - data['Close'].ewm(span=slow_period, adjust=False).mean()
    data['Signal_Line'] = data['MACD_Line'].ewm(span=signal_period, adjust=False).mean()
    return data
