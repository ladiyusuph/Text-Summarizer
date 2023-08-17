import os
from box.exceptions import BoxValueError
import yaml
from txtSummarizer.logging import logger
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
from box import ConfigBox
@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """
    Read yaml file and return a Box object
    
    Args:
        path_to_yaml (Path): Path to yaml file

    Returns:
        ConfigBox: Box object
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info(f"Config: {config}")
            return ConfigBox(config)
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        raise e
    except BoxValueError as e:
        logger.error(f"BoxValueError: {e}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {e}")
        raise e
    

@ensure_annotations
def create_directory(path_to_directory: list, verbose=True):
    """
    Create directory if it does not exist
    
    Args:
        path_to_directory (list): List of paths to create
        verbose (bool, optional): Whether to print out info. Defaults to True.
    """
    for path in path_to_directory:
        if not os.path.exists(path):
            os.makedirs(path)
            if verbose:
                logger.info(f"Created directory: {path}")
        else:
            if verbose:
                logger.info(f"Directory already exists: {path}")


@ensure_annotations
def get_size(path:Path) -> str:
    """
    Get size of file or directory
    
    Args:
        path (Path): Path to file or directory

    Returns:
        str: Size of file or directory
    """
    size_in_kb = round(os.path.getsize(path) / 1024, 3)
    return f"{size_in_kb} KB"