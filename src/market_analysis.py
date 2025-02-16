import pandas as pd

def analyze_market_trends(market_data):
    """
    Analyze market trends (e.g., market size, growth rates).
    """
    # Calculate market size and growth rates
    market_data["market_size"] = market_data["revenue"] * market_data["growth_rate"]
    market_data["growth_rate_pct"] = market_data["growth_rate"] * 100

    return market_data