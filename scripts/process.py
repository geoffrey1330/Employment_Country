import os
import pandas as pd

url = f'https://docs.google.com/spreadsheets/d/1QvbKTaxOgB0Sdb09MNRDpIiiPWqsnmiVpwH7mCAfue4/gviz/tq?tqx=out:csv'

df = pd.read_csv(url)

path = os.getcwd()

file_path = ''.join(path) + '/data/' + 'employment.csv'

# save the csv to the dataset folder
df.to_csv(file_path, index=False)
