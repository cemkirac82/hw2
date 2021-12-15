import os
import pandas as pd

os.chdir('C:/Users/CKIRAC15')

def test(file_path):
    try:
        a=os.path.isfile(file_path)
        pd.read_csv(file_path)
        print('File exists')
    except:
        if FileNotFoundError:
            if a:
                print('File exists')
            else:
                print('File does not exist')
    try:
        with open(file_path) as file: 
            data = file.read()[0]
            print('Data exists')    
    except:
        if IndexError:
            print('There is no data in the file')





