import yfinance as yf # https://pypi.org/project/yfinance/

def getData():
    data = yf.download("^GSPC", period="1mo")
    return data
