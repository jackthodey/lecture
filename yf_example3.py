""" yf_example3.py

qan_prc_to_csv """

import os
import toolkit_config as cfg
import yf_example2

""" qan_prc_to_csv 
This function takes a single (mandatory) parameter called year, an integer.

Purpose: Download Qantas stock prices for a given year into a CSV file

The name of this file will be qan_prc_YYYY.csv, where the YYYY stands for the year in year.

 This file will be saved under the data folder. Remember that the location of this folder is already in the toolkit_config module.

"""
def qan_prc_to_csv(year):
    start = '{}-01-01'.format(year)
    end ='{}-12-31'.format(year)
    tic = 'QAN.AX'
    pth = os.path.join(cfg.DATADIR, 'qan_prc_{}.csv'.format(year))
    yf_example2.yf_prc_to_csv(tic, pth, start, end)


if __name__ == "__main__":
    qan_prc_to_csv(2020)