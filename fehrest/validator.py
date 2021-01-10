import os


def validate_pelican() -> bool:
    from importlib.util import find_spec
    from sys import modules
    return ('pelican' in modules) or find_spec('pelican')


def validate_working_path(path: str) -> bool:
    from os import path as p
    return p.isfile('{}/pelicanconf.py'.format(path)) \
        and p.isdir('{}/content/files'.format(path)) \
        and p.isdir('{}/content/pages'.format(path))


def validate_initialization_path(path: str) -> bool:
    # Checking for emptiness
    from os import path as p
    if p.exists(path):
        root = os.walk(path).__next__()
        return not root[1] and not root[2]
    return True
