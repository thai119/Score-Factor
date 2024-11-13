import os

import pandas as pd
import matplotlib.pyplot
from sklearn.ensemble import RandomForestClassifier

import csv

def convert_csv_to_dataframe(csv_file_path):
    df = pd.read_csv(csv_file_path,on_bad_lines='skip')
    df.to_csv(csv_file_path)

def count_label(apt_file):
    df = pd.read_csv(apt_file)
    print(f'File: {apt_file}')
    print('Label counting:')
    print(df['Stage'].value_counts())
    print('-------------------------------------------------------------------------')
