#I took help from chat gpt for this code

import numpy as np
from scipy.stats import chi2

observed_counts_1 = [4, 10, 10, 13, 20, 18, 18, 11, 13, 14, 13]
observed_counts_2 = [3, 7, 11, 15, 19, 24, 21, 17, 13, 9, 5]
expected_counts=[4,8,12,16,20,24,20,16,12,8,4]
def chi_square_test(observed_counts):
    total_trials = sum(observed_counts)
    temp_list=[((oc-ec)**2)/ec for oc,ec in zip(observed_counts,expected_counts)]
    chi_sq_statistic=sum(temp_list)
    df = len(observed_counts) - 1
    if chi_sq_statistic>chi2.ppf(0.99,df) or chi_sq_statistic<chi2.ppf(0.01,df):
        return chi_sq_statistic,"Not sufficiently random"
    elif chi_sq_statistic>chi2.ppf(0.95,df) or chi_sq_statistic<chi2.ppf(0.05,df):
        return chi_sq_statistic,"Suspect"
    elif chi_sq_statistic>chi2.ppf(0.90,df) or chi_sq_statistic<chi2.ppf(0.10,df):
        return chi_sq_statistic,"Almost suspect"
    else:
        return chi_sq_statistic,"Sufficiently random"


result_1 = chi_square_test(observed_counts_1)
result_2 = chi_square_test(observed_counts_2)

print("Result for run 1: chi2=%f, result=%s"%(result_1[0],result_1[1]))
print("Result for run 2: chi2=%f, result=%s"%(result_2[0],result_2[1]))

