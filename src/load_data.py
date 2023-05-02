# read data from data source
# saved it in the data/raw for further process
import os
import argparse
from get_data import read_params_, get_data_

def load_and_save(config_path):
    config = read_params_(config_path)
    df = get_data_(config_path)
    #new_cols =  df.columns
   # col.replace(" ", "_")
    print(df)

    #raw_data_path= config["load_data"]["raw_dataset_csv"]

    #df.to_csv(raw_data_path, sep=",", index=False, header=new_cols)
    
if __name__ =="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path = parsed_args.config)