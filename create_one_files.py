import csv_combine
import os

root = os.path.dirname(os.path.realpath('create_one_files.py'))


# use def concatinateCSVs(folderPath, ignore_list=[]): in csv_combine.py
# to combine all csv files in the folderPath battery_alt_dataset_regular_alt_batteries, /second_life_batteries, and /recommissoned_batteries
# and save the combined csv files to /battery_alt_dataset/

csv_paths = ['/battery_alt_dataset/regular_alt_batteries',
             '/battery_alt_dataset/second_life_batteries',
             '/battery_alt_dataset/recommissoned_batteries']
for csv_path in csv_paths:
    csv_combine.concatinateCSVs(root+ csv_path, ignore_list=[]).to_csv(root + csv_path + '.csv', index=False)
