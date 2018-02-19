import csv, sys
from datetime import datetime
import pandas as pd

def calc_mvg_avg(econ_data, col):
    with open(econ_data) as ff:
        ffrd = csv.reader(ff)
        next(ffrd)
        for row in ffrd:
            print(row)

def rolling_mean(df):
    print(list(df))
    a = df[' unemployment'].pct_change(periods=11)
    b = df[' inflation'].pct_change(periods=11)
    df['unempl_pct_chg'] = a
    df['infl_pct_chg'] = b
    print(a)
    #df.to_csv('data_frame.csv', sep=',')

def current_econ(df):
    a = df['unemployment'].pct_change(periods=11)
    b = df['inflation'].pct_change(periods=11)
    c = df['tbill'].pct_change(periods=11)
    d = df['natsales'].pct_change(periods=11)
    df['unempl_pct_chg'] = a
    df['infl_pct_chg'] = b
    df['tbill_pct_chg'] = c
    df['natsales_pct_chg'] = d
    df.to_csv('current_econ_mvg_avg.csv', sep=',')
    print(a,b,c,d)

econ_data = "econ_percentages.csv"
current_econ_data = "current_econ_data.csv"
col = 2

if __name__ == "__main__":
    #calc_mvg_avg(econ_data, col)
    econ_df = pd.read_csv(econ_data)
    curr_df = pd.read_csv(current_econ_data)
    rolling_mean(econ_df)
    #current_econ(curr_df)
