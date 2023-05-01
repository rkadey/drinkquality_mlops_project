# read data from data source
# saved it in the data/raw for further process
import os
import argparse
from get_data import read_params, get_data

def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    new_cols = [col.replace(" ", "_") for col in df.columns]
    raw_data_path= config["load_data"]["raw_dataset_csv"]