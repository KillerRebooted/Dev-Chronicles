import os
import matplotlib.pyplot as plt

try:

    import mplcursors
    import yfinance as yf
    import mplfinance as mpf
    import pandas as pd

except:

    os.system("pip install mplfinance")
    os.system("pip install mplcursors")
    os.system("pip install yfinance")
    os.system("pip install pandas")

    import mplcursors
    import yfinance as yf
    import mplfinance as mpf
    import pandas as pd

data_loc = os.path.dirname(os.path.realpath(__file__))

stocks = pd.read_csv(f"{data_loc}/Data/Tickers.csv")

def get_stock_data(ticker, period, interval):
    hist = yf.Ticker(ticker).history(period=period, interval=interval)
    return hist

def on_move(event):
    global x, y

    ax = event.inaxes
    if ax is not None:
        # convert x y device coordinates to axes data coordinates
        x, y = ax.transData.inverted().transform([event.x, event.y])

def make_graph(ticker, period, interval):

    data = get_stock_data(ticker, period, interval)

    custom_style = mpf.make_mpf_style(base_mpf_style='nightclouds', facecolor="#0f0f0f")

    fig, axlist = mpf.plot(data, type="line", style=custom_style, ylabel='Price (in $)', volume=False, linecolor="cyan", returnfig=True)

    mplcursors.cursor(fig, hover=True).connect("add", lambda sel: sel.annotation.set_text(f"${sel.target[1]:.2f}"))

    fig.canvas.mpl_connect('motion_notify_event', on_move)
    
    rect = fig.patch
    rect.set_facecolor('#0f0f0f')

    return fig

def search_from_name(search, ticker=False):

    if ticker: recommendation_number = 1
    else: recommendation_number = 10

    symbols = {}

    for ticker in stocks[stocks["Symbol"].str.contains(search, case=False)]["Symbol"][:recommendation_number]:
        symbols[ticker] = stocks[stocks["Symbol"] == ticker]["Security Name"].values[0]

    for ticker in stocks[stocks["Security Name"].str.contains(search, case=False)]["Symbol"][:recommendation_number-len(symbols)]:
        symbols[ticker] = stocks[stocks["Symbol"] == ticker]["Security Name"].values[0]

    return symbols

def get_ticker_details(ticker):

    stock = yf.Ticker(ticker)

    info = stock.info

    latest_price = stock.history(period='5d', interval='1d').tail(1)['Close'].values[0]

    info["latest_price"] = f"{latest_price:.2f}"

    required_details = {"Symbol": "symbol", "Latest Price": "latest_price", "52W High": "fiftyTwoWeekHigh", "52W Low": "fiftyTwoWeekLow", "Total Revenue": "totalRevenue", "Market Cap": "marketCap", "Volume": "volume", "Country": "country", "State": "state", "Website": "website", "Industry": "industry", "Sector": "sector", "Business Summary": "longBusinessSummary"}

    results = {}

    for k, v in required_details.items():
        try:
            results[k] = info[v]
        except:
            pass

    return results

if __name__ == "__main__":

    ticker = list(search_from_name("GBIL").keys())[0]

    make_graph(ticker, "ytd", "1d")
    plt.show()

    for i in ([f"{k}: {v}" for k, v in get_ticker_details(ticker).items()]):
        print(i)