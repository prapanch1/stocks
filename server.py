import yfinance as yf
from colorama import Fore
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("yfinanceserver")

@mcp.tool()
def stock_price(stock_ticker: str) -> str:
    dat = yf.Ticker(stock_ticker)
    historical_prices = dat.history(period='1mo')
    last_months_closes = historical_prices['Close']
    print(Fore.YELLOW + str(last_months_closes))
    return str(f"Stock price over the last month for {stock_ticker}: {last_months_closes}")

if __name__ == "__main__":
    mcp.run(transport="stdio")