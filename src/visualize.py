import matplotlib.pyplot as plt
import plotly.express as px

def plot_market_trends(market_data):
    """
    Plot market size and growth rates.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(market_data["sector"], market_data["market_size"])
    plt.title("Market Size by Sector")
    plt.xlabel("Sector")
    plt.ylabel("Market Size ($)")
    plt.show()

def plot_industry_dynamics(industry_data):
    """
    Plot market share by company.
    """
    fig = px.bar(industry_data, x="company", y="market_share", color="sector", title="Market Share by Company")
    fig.show()