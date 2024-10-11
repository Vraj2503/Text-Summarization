import yaml
import os
from wordSummerizer.logging import logger
from box.exceptions import BoxValueError
from box import ConfigBox
'''
ConfigBox is used where you want to access the value of a dictionary using the key as "d.key"
insted of d['key'] as it is more convinient to use it that way.
ConfigBox is a way to store key and values, other than a dictionary.
'''
from pathlib import Path
from typing import Any    #This allows us to declare a variable of type Any(Literally anything)

'''
Ensure Annotations ensure that the arguments passed in the functions match the type that 
is originally declared. Just like typescript (if I am not wrong).
'''

def read_yaml(path_to_yaml: str) -> ConfigBox:
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            config = yaml.safe_load(yaml_file)
            return ConfigBox(config)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


        