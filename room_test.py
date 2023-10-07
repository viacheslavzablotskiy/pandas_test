from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

from glob import glob
from os.path import abspath

download_url = 'https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json'
path_to_your_plots = './plots'


class DrawingPlots:
    def __init__(self):
        self.download_url = download_url
        self.path_to_your_plots = path_to_your_plots

    def read_json(self):
        data = pd.read_json(self.download_url, orient='columns')
        return data

    def return_all_path_of_our_plots(self):
        for file_name in glob(self.path_to_your_plots):
            print(file_name, '->', abspath(file_name))

    def create_plot(self, first_name_column, second_name_column, name_your_plot):
        time_now = datetime.now()
        try:
            data = self.read_json()
            data.plot(x=f'{first_name_column}', y=f'{second_name_column}', kind='scatter')
            # example for Notebook.ipynb because it dont work in Pycharm(only in Pycharm Profesional)
            # plt.figure(figsize=(10,6))
            # sns.scatterplot(x=data[f'{first_name_column}'], y=data[f'{second_name_column}']
            # sns.lmplot(x=f'{first_name_column}', y=f'{second_name_column}', data=data)
            # plt.show()
            plt.savefig(f'./plots/{name_your_plot}_{str(time_now)}')
            return plt.show()
        except InterruptedError:
            print('Error, why? Idk')


your_class = DrawingPlots()
your_operation = str(input())
if your_operation == 'create_plots':
    name_column_one = str(input())
    name_column_second = str(input())
    name_your_plots = str(input())
    your_class.create_plot(name_your_plots, name_column_second, name_your_plots)
elif your_operation == 'return all path':
    your_class.return_all_path_of_our_plots()
else:
    print('your operation be unknown')
