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
            if is_ignored(full):
                continue
            if entry.is_file(follow_symlinks=False):
                with open(full, 'rb') as f:
                    print(data.hash_object(f.read()), full)
                print(full)
            elif entry.is_dir(follow_symlinks=False):
                write_tree(full)


def is_ignored(path):
    return '.mygit' in path.split('/')
