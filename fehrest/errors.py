import sys

INVALID_WORKING_DIR = 1
NO_FILES = 2
INVALID_INIT_DIR = 3

__errors = {
    INVALID_WORKING_DIR: 'The working directory in not valid.',
    NO_FILES: 'Publish failed. No content file is available. Copy your content file into the content folder.',
    INVALID_INIT_DIR: 'The specified path in not empty.'
}


def raise_error(code: int):
    print(__errors[code])
    sys.exit(1)
