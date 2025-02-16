import pandas as pd

def benchmark_companies(industry_data, target_company):
    """
    Benchmark a target company against industry peers.
    """
    # Filter data for the target company
    target_data = industry_data[industry_data["company"] == target_company]

    # Compare with industry averages
    industry_avg = industry_data.groupby("sector").mean()
    benchmark_results = pd.merge(target_data, industry_avg, on="sector", suffixes=("_target", "_industry"))

    return benchmark_results