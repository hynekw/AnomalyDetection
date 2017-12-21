import pandas as pd
import numpy as np
import datetime
from anomaly_detection import anomaly_detect_vec


# import test data and try it!
def dparserfunc(date):
    return pd.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')


test_data = pd.read_csv('~/Git/GH/AnomalyDetection/tests/test_data.csv',
                        index_col='timestamp', parse_dates=True, squeeze=True,
                        date_parser=dparserfunc)

test_kiwi = pd.read_csv('~/Desktop/kiwi_to_py.csv', index_col='time',
                        parse_dates=True, squeeze=True,
                        date_parser=dparserfunc)




test_res = anomaly_detect_vec(test_kiwi, max_anoms=0.05, direction="both",
                              alpha=0.05, period=24, only_last=False,
                              plot=False)
