from glob import glob
import pandas as pd
import numpy as np

target_dict = {'1a': 1, '1b': 2, '2a': 3, '2b': 4,'2c': 5, '2d': 6, '3a': 7, '3b': 8}

def handle_missing_values(df):
    df['AccX']=df['AccX'].replace(0, np.nan)
    df['AccY']=df['AccY'].replace(0, np.nan)
    df['AccZ']=df['AccZ'].replace(0, np.nan)

    df['GyroX']=df['GyroX'].replace(0, np.nan)
    df['GyroY']=df['GyroY'].replace(0, np.nan)
    df['GyroZ']=df['GyroZ'].replace(0, np.nan)

    df['MagX']=df['MagX'].replace(0, np.nan)
    df['MagY']=df['MagY'].replace(0, np.nan)
    df['MagZ']=df['MagZ'].replace(0, np.nan)
    return df


def load_data(csv_folder_path):
    """

    :param csv_folder_path:
    :return:
    """
    csv_file_paths = glob(csv_folder_path)
    y_list = []
    x_data_list = []

    for csv_file in csv_file_paths:
        csv_df = pd.read_csv(csv_file)
        csv_df = handle_missing_values(csv_df)
        csv_df.dropna(inplace=True)
        target_label = csv_df.values[0][10]
        y = target_dict[target_label]
        y_list.append(y)
        x_data_list.append(csv_df.drop(["timestamp","Activity"],axis=1).values)

    return x_data_list,y_list

if __name__ == "__main__":
    x_data,y = load_data("segdata/0003/*")
    print(y)
    print(x_data)