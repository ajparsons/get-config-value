import json
import os
from pathlib import Path

import toml
from ruamel.yaml import YAML

yaml=YAML(typ='safe')

def get_data(file_path: str) -> dict:
    """
    Get relevant data file based on extention
    """
    match Path(file_path).suffix.lower():
        case ".json":
            loader = json.load
        case ".yaml" | ".yml":
            loader = yaml.load
        case ".toml":
            loader = toml.load
        case e:
            raise ValueError(f"No loader configured for {e}")

    with open(file_path) as stream:
        data = loader(stream)
    
    return data

def add_to_step_output(**kwargs):
    """
    Add kwargs to the step outputs
    """
    with open(os.environ["GITHUB_OUTPUT"], 'a') as f:
        for k, v in kwargs.items():
            f.write(f'\n{k}={v}')

def get_value(file_path: str, key: str):
    """
    Get data based on key
    """

    data = get_data(file_path)

    for k in key.split("."):
        data = data[k]
        if isinstance(data, list):
            data = {str(x):y for x,y in enumerate(data)}

    print(f"From {file_path}, read {key}, result: {data}")

    add_to_step_output(value=data)

if __name__ == "__main__":
    
    get_value(os.environ["CONFIG_FILE"], os.environ["CONFIG_KEY"])