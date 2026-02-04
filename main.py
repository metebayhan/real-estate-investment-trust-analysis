import numpy as np

adj_closings_sbra = np.loadtxt("SBRA.csv", skiprows=1, usecols=5, delimiter=',')
adj_closings_eqr = np.loadtxt("EQR.csv", skiprows=1, usecols=5, delimiter=',')

def rate_of_return(adj_closings):
    daily_simple_ror = np.diff(adj_closings) / adj_closings[:-1]
    return daily_simple_ror

daily_simple_returns_sbra = rate_of_return(adj_closings_sbra)
daily_simple_returns_eqr = rate_of_return(adj_closings_eqr)

print(daily_simple_returns_sbra)
print(daily_simple_returns_eqr)

average_daily_simple_return_sbra = np.mean(daily_simple_returns_sbra)
print("Average Daily Simple Return of SBRA: ", average_daily_simple_return_sbra)
average_daily_simple_return_eqr = np.mean(daily_simple_returns_eqr)
print("Average Daily Simple Return of EQR: ", average_daily_simple_return_eqr)

def log_returns(adj_closings):
    log_adj_closings = np.log(adj_closings)
    daily_log_returns = np.diff(log_adj_closings)
    return daily_log_returns

daily_log_returns_sbra = log_returns(adj_closings_sbra)
daily_log_returns_eqr = log_returns(adj_closings_eqr)

def annualize_log_return(daily_log_returns):
    average_daily_log_return = np.mean(daily_log_returns)
    annualized_log_return = average_daily_log_return * 252
    return annualized_log_return

annualized_log_return_sbra = annualize_log_return(daily_log_returns_sbra)
print("Annually Log Return of SBRA: ", annualized_log_return_sbra)
annualized_log_return_eqr = annualize_log_return(daily_log_returns_eqr)
print("Annually Log Return of EQR: ", annualized_log_return_eqr)

daily_variance_sbra = np.var(daily_log_returns_sbra, ddof=1)
print("Daily Variance of SBRA ", daily_variance_sbra)
daily_variance_eqr = np.var(daily_log_returns_eqr, ddof=1)
print("Daily Variance of EQR ", daily_variance_eqr)

daily_sd_sbra = np.std(daily_log_returns_sbra, ddof=1)
print("Daily Standard Deviation of SBRA ", daily_sd_sbra)
daily_sd_eqr = np.std(daily_log_returns_eqr, ddof=1)
print("Daily Standard Deviation of EQR ", daily_sd_eqr)

corr_sbra_eqr = np.corrcoef(daily_log_returns_sbra, daily_log_returns_eqr)
corr = corr_sbra_eqr[0,1]
print("The Corelation of Between SBRA and EQR: ", corr)
