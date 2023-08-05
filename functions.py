import math
import pandas as pd

def perform_match_exact(row, df , *args):
    # row is the the item that we want to match
    # df is the source Pandas dataframe that we want to match it with other items
    # print('Start matching')
    sub_set = df
    
    for arg in args:
        sub_set = sub_set.loc[sub_set[arg] == row[arg]]
        # print(sub_set)
        
    return sub_set.index


def logit(p):
    return math.log(p / (1-p))

def hasCabin(x):
    return 0 if pd.isna(x) else 1
    
def cohenD(tmp, metricName):
    treated_metric = tmp[tmp.treatment == 1][metricName]
    untreated_metric = tmp[tmp.treatment == 0][metricName]

    return (treated_metric.mean() - untreated_metric.mean()) / math.sqrt(
        (
            (treated_metric.count() - 1) * treated_metric.std() ** 2
            + (untreated_metric.count() - 1) * untreated_metric.std() ** 2
        )
        / (treated_metric.count() + untreated_metric.count() - 2)
    )