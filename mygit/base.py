# This module will have the basic higher-level logic of ugit.
import os

from . import data

def write_tree(directory='.'):
    """
    Write a tree object from the contents of the given directory.
    @param directory: The directory to write the tree from.
    """
    entries = []
    with os.scandir(directory) as it:
        for entry in it:
            full = f'{directory}/{entry.name}'
            if is_ignored(full):
                continue

            type_ = None
            oid = None

            if entry.is_file(follow_symlinks=False):
                type_ = 'blob'
                with open(full, 'rb') as f:
                    oid = data.hash_object(f.read())
            elif entry.is_dir(follow_symlinks=False):
                type_ = 'tree'
                oid = write_tree(full)

            if type_ is not None and oid is not None:
                entries.append((entry.name, oid, type_))

    tree = ''.join(f'{type_} {oid} {name}\n' for name, oid, type_ in sorted(entries))
    return data.hash_object(tree.encode(), 'tree')


def is_ignored(path):
    return '.mygit' in path.split('/')
