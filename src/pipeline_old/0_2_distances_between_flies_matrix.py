import os
import pandas as pd 
import package_functions as hf
from config_constants import DATA_PATH

#DATA_PATH = '../2_pipeline/0_0_preproc_data/out'

SAVE_PATH = './2_pipeline/0_2_distances_between_flies_matrix/out'

os.makedirs(SAVE_PATH, exist_ok=True)

experiments = hf.load_multiple_folders(DATA_PATH)

for pop_name, path in experiments.items():  
    
    min_x, min_y = hf.find_pop_mins(path)
    
    list_of_dataframes = hf.load_dfs_to_list(path, min_x, min_y)
    distances_between_all_flies = hf.distances_between_all_flies(list_of_dataframes)
    distances_between_all_flies.to_csv(SAVE_PATH + '/' + pop_name + '.csv')
    