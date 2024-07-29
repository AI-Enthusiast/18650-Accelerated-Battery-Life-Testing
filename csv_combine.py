import os
import glob # pip install glob2
import pandas as pd
import warnings
import time
import tqdm # pip install tqdm

csv_paths = ['/battery_alt_dataset/regular_alt_batteries',
             '/battery_alt_dataset/second_life_batteries',
             '/battery_alt_dataset/recommissioned_batteries']

root = os.path.dirname(os.path.realpath('csv_combine.py'))


def concatinateCSVs(folderPath, ignore_list=[]): # combines all csv files in a folder into df
    # print('concatinating csvs in', folderPath)
    root = os.path.dirname(os.path.realpath('csv_combine.py'))
    warnings.filterwarnings("ignore")
    os.chdir(folderPath)
    # all the filenames with a .csv format
    allFilenames = [i for i in glob.glob("*.{}".format("csv"))]
    combinedFilesData = []
    for file in tqdm.tqdm(allFilenames, desc='Combining ' + folderPath.split('/')[-1]):
        if file in ignore_list:
            continue
        try:
            combinedFilesData.append(pd.read_csv(file))
        except pd.errors.EmptyDataError:
            print(file, "is empty")
            # os.remove(f)
            # print(f, "has been deleted")
            continue
        except pd.errors.ParserError:
            print(file, "parse error")
            continue
    try:  # concatinate all csv data in a folder
        combinedFilesData = pd.concat([file for file in combinedFilesData], )
    except ValueError:
        combinedFilesData = []
    os.chdir(root)
    return pd.DataFrame(combinedFilesData)


def combine_csvs(csv_paths): # builds the one files from folders
    for csv_path in csv_paths:
        concatinateCSVs(root + csv_path, ignore_list=[]).to_csv(root + csv_path + '.csv', index=False)
    return


def convert_to_preferred_format(sec):  # only to be fancy
    sec = sec % (24 * 3600)
    sec %= 3600
    min = sec // 60
    sec %= 60
    # print("seconds value in minutes:",min)
    return "%02d:%02d" % (min, sec)


if __name__ == '__main__':
    start_time = time.time()
    combine_csvs(csv_paths)
    print('Time taken:', convert_to_preferred_format(time.time() - start_time))
