import os
from ruamel.yaml import YAML

def add_to_step_output(**kwargs):
    """
    Add kwargs to the step outputs
    """
    with open(os.environ["GITHUB_OUTPUT"], 'a') as f:
        for k, v in kwargs.items():
            f.write(f'\n{k}={v}')

def get_value(file_path: str, key: str):

    yaml=YAML(typ='safe')

    with open(file_path) as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    for k in key.split("."):
        data = data[k]
        if isinstance(data, list):
            data = {str(x):y for x,y in enumerate(data)}

    add_to_step_output(value=data)

if __name__ == "__main__":
    
    get_value(os.environ["YAML_FILE"], os.environ["YAML_KEY"])

