import os
import glob
import pandas as pd
import warnings

def concatinateCSVs(folderPath, ignore_list=[]):
    # print('concatinating csvs in', folderPath)
    root = os.path.dirname(os.path.realpath('csv_combine.py'))
    warnings.filterwarnings("ignore")
    os.chdir(folderPath)
    # all the filenames with a .csv format
    allFilenames = [i for i in glob.glob("*.{}".format("csv"))]
    combinedFilesData = []
    for file in allFilenames:
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