import matplotlib.pyplot as plt
import pandas as pd


def create_and_save_plot(data, ticker, period, filename=None):
    """
    Создает и сохраняет график для отображения цены акции, скользящей средней, RSI и MACD.
    
    Args:
        data (pandas.DataFrame): Данные с колонками "Close", "Moving_Average", "RSI", "MACD_Line", "Signal_Line".
        ticker (str): Биржевой тикер компании.
        period (str): Период данных (например, "1mo").
        filename (str, optional): Имя файла для сохранения графика. Если None, генерируется автоматически.
    
    Saves:
        Файл с графиком в формате PNG.
    """
    plt.figure(figsize=(14, 10))

    # Если Date отсутствует, создаем его из индекса
    if 'Date' not in data.columns:
        data = data.reset_index()

    # Первое окно: Цена акций и скользящая средняя
    plt.subplot(3, 1, 1)
    plt.plot(data['Date'], data['Close'], label='Close Price')
    if 'Moving_Average' in data.columns:
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    # Второе окно: RSI
    if 'RSI' in data.columns:
        plt.subplot(3, 1, 2)
        plt.plot(data['Date'], data['RSI'], label='RSI', color='orange')
        plt.axhline(70, color='red', linestyle='--', linewidth=1)
        plt.axhline(30, color='green', linestyle='--', linewidth=1)
        plt.title("RSI")
        plt.xlabel("Дата")
        plt.ylabel("Значение RSI")
        plt.legend()

    # Третье окно: MACD
    if 'MACD_Line' in data.columns and 'Signal_Line' in data.columns:
        plt.subplot(3, 1, 3)
        plt.plot(data['Date'], data['MACD_Line'], label='MACD Line', color='blue')
        plt.plot(data['Date'], data['Signal_Line'], label='Signal Line', color='red')
        plt.bar(data['Date'], data['MACD_Line'] - data['Signal_Line'], label='Histogram', color='gray', alpha=0.5)
        plt.title("MACD")
        plt.xlabel("Дата")
        plt.ylabel("MACD")
        plt.legend()

    plt.tight_layout()

    if filename is None:
        filename = f"{ticker}_{period}_stock_indicators.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")
