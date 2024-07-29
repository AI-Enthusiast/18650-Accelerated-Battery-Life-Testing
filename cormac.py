import os
import pandas as pd

root = os.path.dirname(os.path.realpath('cormac.py'))

TEST = True

if TEST:
    data_path = root + '/battery_alt_dataset/regular_alt_batteries/battery00.csv'
    print('Running in test mode')
else:
    data_path = root + '/battery_alt_dataset/regular_alt_batteries.csv'
print('data_path:', data_path)

data = pd.read_csv(data_path)

print(data.head())