import os
import glob  # pip install glob2
import pandas as pd
import warnings
import time
import tqdm  # pip install tqdm

# * 9.30A: Battery pack 0.1 and 1.1
# * 12.9A: Battery pack 3.1 and 2.2
# * 14.3A: Battery pack 2.3 and 5.2
# * 16.0A: Battery pack 0.0 and 1.0
# * 19.0A: Battery pack 2.0, 3.0 and 2.1

csv_paths = ['/battery_alt_dataset/regular_alt_batteries',
             '/battery_alt_dataset/second_life_batteries',
             '/battery_alt_dataset/recommissioned_batteries']

root = os.path.dirname(os.path.realpath('csv_combine.py'))


def concatinateCSVs(folderPath, ignore_list=[]):  # combines all csv files in a folder into df
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
            df = pd.read_csv(file)
            # # drop all rows except the one with the greatest time value
            # df = df.drop_duplicates(subset=['time'], keep='last')
            combinedFilesData.append(df)
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


def combine_csvs(csv_paths):  # builds the one files from folders
    for csv_path in csv_paths:
        (concatinateCSVs(root + csv_path,
                         ignore_list=['battery40.csv', 'battery41.csv',
                                      'battery50.csv', 'battery51.csv']).
         to_csv(root + csv_path + '.csv', index=False))
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
