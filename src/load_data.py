# read data from data source
# saved it in the data/raw for further process
import os
import argparse
from get_data import read_params__, get_data__

def load_and_save(config_path):
    config = read_params__(config_path)
    data = get_data__(config_path)
    new_cols = [col.replace(" ", "_") for col in data.columns] 
    print(new_cols)

   # raw_data_path= config["load_data"]["raw_dataset_csv"]

   # df.to_csv(raw_data_path, sep=",", index=False, header=new_cols)
    
if __name__ =="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path = parsed_args.config)