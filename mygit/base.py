# This module will have the basic higher-level logic of ugit. 
import os

from . import data

def write_tree(directory='.'):
    """
    Write a tree object from the contents of the given directory.
    @param directory: The directory to write the tree from.
    """
    with os.scandir(directory) as it:
        for entry in it:
            full = f'{directory}/{entry.name}'
            if entry.is_file(follow_symlinks=False):
                # TODO: write the file to object store
                print(full)
            elif entry.is_dir(follow_symlinks=False):
                write_tree(full)
    