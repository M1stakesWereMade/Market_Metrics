import data_download as dd
import data_plotting as dplt


def main():
    """
    Главная функция программы. Запрашивает данные у пользователя, загружает биржевые данные,
    рассчитывает технические индикаторы и отображает их на графике.
    """
    print("Добро пожаловать в StockInsight - инструмент анализа биржевых данных.")
    print("Примеры тикеров: AAPL, GOOGL, MSFT, AMZN, TSLA.")
    print("Примеры периодов: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, макс.")

    ticker = input("Введите тикер акции (например, «AAPL»): ")
    period = input("Введите период для данных (например, '1mo'): ")

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add indicators
    stock_data = dd.add_moving_average(stock_data)
    stock_data = dd.calculate_rsi(stock_data)
    stock_data = dd.calculate_macd(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)


if __name__ == "__main__":
    main()
