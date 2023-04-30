## read params
## process data
## return dataframe
import os
import yaml
import pandas as pd
import argparse



    

    
if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()

