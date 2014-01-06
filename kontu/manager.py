import json

from models.manager import Project


def load_project(route):
    """
    Loads a project file and return a new Project instance without saving.
    """
    config = None
    with open(route) as config_file:
        config = config_file.read()
    if config:
        obligatory_keys = ['name']
        config = json.loads(config)
        for key in obligatory_keys:
            if not key in config:
                raise ValueError("Key '{0}' not found in config file".format(key))
    project = Project(**config)
    return project
