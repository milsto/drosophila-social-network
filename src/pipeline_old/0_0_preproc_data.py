import os
import pandas as pd
import package_functions as hf
from config_constants import EXPERIMENT_DURATION, FPS, DATA_PATH

DATAFRAME_LEN = EXPERIMENT_DURATION * FPS

SAVE_PATH = './2_pipeline/0_0_preproc_data/out'

experiments = hf.load_multiple_folders(DATA_PATH)

for pop_name, path in experiments.items():  

    if not hf.check_data(path):
        continue    
    
    if not os.path.exists(SAVE_PATH + '/' + pop_name):
        os.makedirs(SAVE_PATH + '/' + pop_name)
        
    fly_dict = hf.load_files_from_folder(path)
    
    #hf.inspect_population_coordinates(path, pop_name)
    
    min_x, min_y = hf.find_pop_mins(path)
    
    for fly_name, path in fly_dict.items(): 
        
        df = pd.read_csv(path)
        df = df.head(DATAFRAME_LEN)
        df = hf.prepproc(df, min_x, min_y)
        df = hf.round_coordinates(df, decimal_places=0)
        
        df.to_csv(SAVE_PATH + '/' + pop_name + '/' + fly_name)
    

        

        